import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, Sequence

import requests  # Import requests
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequestParams,
    CallToolRequest,
    CallToolResult,
    ClientCapabilities,
    EmbeddedResource,
    ImageContent,
    ListToolsRequest,
    ListToolsResult,
    Prompt,
    PromptArgument,
    PromptMessage,
    RootsCapability,
    ServerCapabilities,
    TextContent,
    Tool,
)
from pydantic import BaseModel, Field, AnyUrl
from mcp.shared.exceptions import McpError


# Configuration for Server A and Server B (using URLs for HTTP communication)
SERVER_A = {
    "url": "http://localhost:5000/mcp/v1", # URL of Server A
    "tool_name": "ask_personal_trainer", # Tool name on Server A
}
SERVER_B = {
    "url": "http://localhost:5001/mcp/v1",  # Replace with actual URL for Server B
    "tool_name": "handle_professional_task",  # Replace with actual tool name on Server B
}

# Set up logging
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

# Initialize the MCP server
server = Server("gateway-agent")


@server.list_tools()
async def list_tools() -> ListToolsResult:
    # ... (No changes to list_tools)
    pass  # Placeholder for brevity


def ask_mcp_server(server_url: str, tool_call: str, data: str) -> str: # Add type hints
    """Sends an MCP tool call request to the specified server."""
    body = {
        "jsonrpc": "2.0",
        "id": 1,  # Using a static ID for simplicity in this example. In a real application, you should manage IDs.
        "method": "tools/call",
        "params": {
            "name": tool_call,
            "arguments": {"body": data}, # Correct tool call (no nested title, labels, etc.)
        },
    }
    try:
        response = requests.post(server_url, json=body).json()
        print(json.dumps(response, indent=4))
        return response.get("result",{}).get("content",[])[0].get('text')

    except requests.exceptions.RequestException as e:
        raise McpError(INTERNAL_ERROR, f"Error communicating with server: {e}")
    except (KeyError, IndexError) as e:
         raise McpError(INTERNAL_ERROR, f"Unexpected response format: {e}")

@server.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Routes the task to the appropriate server and tool."""

    if name != "route_task":
        raise ValueError(f"Unknown tool: {name}")


    user_input = arguments.get("user_input")
    if not user_input:
        raise ValueError("Missing 'user_input' argument.")



    # Routing logic (can be improved with NLP or more sophisticated methods)
    if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
        target_server = SERVER_A
    else:
        target_server = SERVER_B  # Default server (you'll need to implement server B)


    try:
        # Use the ask_mcp_server function to make the tool call
        result = ask_mcp_server(target_server["url"], target_server["tool_name"], user_input)
        return [TextContent(type="text", text=result)]  # Correctly wrap in TextContent
    except McpError as e:
        raise
    except Exception as e:
        logger.error(f"Error routing task to server: {e}")
        raise McpError(f"Error routing task: {e}")

async def run():
    """Run the gateway agent server."""
   # ... (No changes in run() function)
    pass

def main():
    anyio.run(run)


if __name__ == "__main__":
    main()