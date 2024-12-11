import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, Sequence

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

# Configuration for Server A and Server B
SERVER_A = {
    "url": "http://localhost:5000/mcp/v1",  # URL for Server A's MCP endpoint
    "tool_name": "ask_personal_trainer",      # Tool name on Server A
}
SERVER_B = {
    "url": "http://localhost:5001/mcp/v1", # URL for Server B's MCP endpoint (replace with actual if different)
    "tool_name": "handle_professional_task",  # Tool name on Server B (replace with actual)
}

# Set up logging
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

# Initialize the MCP server
server = Server("gateway-agent")


@server.list_tools()
async def list_tools() -> ListToolsResult:
    return ListToolsResult(
        tools=[
            Tool(
                name="route_task",
                description="""Routes a user's productivity-related query or task to the appropriate agent (Server A or Server B).""",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "user_input": {
                            "type": "string",
                            "description": "User's productivity-related query or task.",
                        },
                    },
                    "required": ["user_input"],
                },
            ),
        ]
    )


async def _run_tool_on_server(server_config: Dict[str, Any], user_input: str) -> CallToolResult:
    """Runs the specified tool on the given server with the provided user input."""

    from mcp.client import ClientSession, sse_client
    
    async with sse_client(server_config["url"]) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            try:
                result = await session.call_tool(
                    server_config["tool_name"], {"body": user_input}
                )
                return result
            except McpError as e:
                return e.error
            except Exception as e:
                logger.error(f"Error running tool on server: {e}")
                raise McpError(f"Error running tool on server: {e}")



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

    # Routing logic based on keywords (customize as needed)
    if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
        target_server = SERVER_A
    elif any(keyword in user_input.lower() for keyword in ["work", "meeting", "deadline", "project"]):
        target_server = SERVER_B
    else:
        target_server = SERVER_B  # Default server

    result = await _run_tool_on_server(target_server, user_input)  # replace this function with the tool call from talk.py in ask_mcp_server in in talk.py n server a)
    
    return [TextContent(type="text", text = result.content[0].text)]

async def run():
    """Run the gateway agent server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="gateway_agent",
                server_version="0.1.0",  # Replace with your version
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def main():
    anyio.run(run)


if __name__ == "__main__":
    main()