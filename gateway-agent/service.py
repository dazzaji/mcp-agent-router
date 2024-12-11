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


# Configuration for Server A and Server B
SERVER_A_CONFIG = {
    "command": "python",
    "args": ["-m", "physical_productivity_agent"],  # Replace with actual module name
}
SERVER_B_CONFIG = {
    "command": "python",
    "args": ["-m", "professional_productivity_agent"],  # Replace with actual module name
}

# Set up logging
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

# Initialize the MCP server
server = Server("gateway-agent")

class RouteArgs(BaseModel):
    user_input: str = Field(..., description="User's productivity-related query or task.")

@server.list_prompts()
async def list_prompts() -> list[Prompt]:
    return [
        Prompt(
            name="route",
            description="Route a productivity task to the appropriate agent.",
            arguments=[
                PromptArgument(
                    name="user_input",
                    description="The user's input or query related to productivity.",
                    required=True,
                ),
            ],
        )
    ]


@server.get_prompt()
async def get_prompt(name: str, arguments: dict | None) -> types.GetPromptResult:
    if name != "route":
        raise ValueError(f"Unknown prompt: {name}")

    user_input = (arguments or {}).get("user_input")
    if not user_input:
        raise ValueError("Missing 'user_input' argument.")


    return types.GetPromptResult(
        description=f"Routing prompt for user input: {user_input}",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text=f"""Decide whether the following user input relates to physical productivity (Server A) or professional/work productivity (Server B):
                    
                    User Input: "{user_input}"
                    
                    Respond with either "Server A" or "Server B".
                    """,
                ),
            )
        ],
    )




@server.list_tools()
async def list_tools() -> ListToolsResult:
    return ListToolsResult(
        tools=[
            Tool(
                name="route_task",
                description="""Routes a user's productivity-related query or task to the appropriate agent (Server A or Server B).""",
                inputSchema=RouteArgs.model_json_schema(),
            ),
        ]
    )


async def _run_tool_on_server(server_config: Dict[str, Any], tool_name: str, arguments: Dict[str, Any]):
    from mcp.client import ClientSession, stdio_client, StdioServerParameters
    
    server_params = StdioServerParameters(command=server_config["command"], args=server_config["args"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            return await session.call_tool(tool_name, arguments)
            

@server.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:

    if name != "route_task":
        raise ValueError(f"Unknown tool: {name}")

    user_input = arguments.get("user_input")
    if not user_input:
        raise ValueError("Missing 'user_input' argument.")

    # Basic routing logic (replace with your actual routing criteria)
    if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
        target_server = SERVER_A_CONFIG
        tool_to_call = "handle_physical_task"  # Tool name on server A
    elif any(keyword in user_input.lower() for keyword in ["work", "meeting", "deadline", "project"]):
        target_server = SERVER_B_CONFIG
        tool_to_call = "handle_professional_task"  # Tool name on server B
    else:
        # Default to server B if no specific keywords are found
        target_server = SERVER_B_CONFIG
        tool_to_call = "handle_professional_task"

    try:
        result = await _run_tool_on_server(target_server, tool_to_call, {"user_input": user_input})
        return result.content
    except Exception as e:
        logger.error(f"Error routing task to server: {e}")
        raise McpError(f"Error routing task: {e}")


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