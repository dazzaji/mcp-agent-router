# MCP Multi-Agent Modular Awesomeness!

## Overview

This is a primative multi-agent modular initialization capability test prototype of Model Context Protocol.  My test project will have multiple servers and clients.  They will operate in a modular way, the first will create a markdown file based on adding user input text to a content template and saving the file to root directory.  The second will ingest that file and add more info to it then save the updated version to the root.  The alt A third will likewise ingest the output of the second and add still more content and export the third version of the file to the root.  The alt B third server alternatively could take another action.  Treat each of these three like back boxes in the sense that they will not share code or components but we will pretend they are running on different technologies to preserve the modular approach and we will for convenience be able to do things like share a virtual environment and requirements for this first test.  The second server will be a decider and will choose which is the best next server.

The notion of strict modularity such that different MCP interoperable system could be created and operated by totally different teams or even different companies is potentially a key unlock for MCP and for LLM based agents to take off and be scalable and more fully userful.  This is described more fully in the project overview for "Agent" here: [https://github.com/dazzaji/mcp-project/issues/1](https://github.com/dazzaji/mcp-project/issues/1). 

## Try it!

Let's get your MCP project running in VS Code with the Inspector and Claude Desktop.

**1. Running in VS Code with MCP Inspector**

Here's how to run your project in VS Code and inspect the communication using MCP Inspector:

* **Install the `mcp` package:**  In your project root (`mcp-project`), ensure you have installed the MCP package in your active virtual environment:

```bash
uv add mcp
```

* **Set up `launch.json`**: You'll need launch configurations for each of your MCP servers.  Since you're simulating "black boxes" that *might* run different underlying technologies, the launch configuration will vary for the Gemini server.  Create a `.vscode/launch.json` file in your project's root directory with the following configurations.  This assumes the gemini-server takes a `model` parameter, which specifies the model to use.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Module 1 Server",
            "type": "python",
            "request": "launch",
            "module": "module1_server.server", // Use module mode for direct execution
            "console": "integratedTerminal"
        },
        {
            "name": "Gemini Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/gemini-server/server.py",
            "args": ["--model", "gemini-pro"], // Example model argument
            "console": "integratedTerminal"
        }
    ]
}
```

*   **Running the servers:**
    *   Open the `module1-server/server.py` file in VS Code.
    *   Start the debugger by pressing `F5` or selecting "Start Debugging" from the "Run" menu, and choose the `Module 1 Server` configuration. This will start the Module 1 server in the VS Code integrated terminal. In a similar way, start the `Gemini Server` in a separate terminal.
    *   In a new terminal at the root of your project, start the gateway agent with `uv run gateway_agent`.


*   **Start MCP Inspector:**
    *   Open a *new* terminal in the `gateway-agent` directory.
    *   Run the following command:

    ```bash
    npx @modelcontextprotocol/inspector python -m gateway_agent
    ```
    *   This starts the MCP Inspector, which automatically launches the gateway-agent server and the Inspector UI. A URL will be printed in the terminal. Open this URL in your browser to access the UI.

    *   In the Inspector UI, click on "Tools" to confirm the tools your gateway agent has registered.

Now you can interact with the servers through the MCP Inspector UI, sending requests and viewing responses and logs. The logging messages from your `service.py` file will appear in the Inspector's console, which can be useful for debugging.  You can test the routing functionality by calling the `route_task` tool with different inputs and observing which downstream server is called.



**2. Running with Claude Desktop**

To use your MCP servers with Claude Desktop:

*   **Install your servers** into your local environment or a Docker container. If you use Docker make sure both the gateway agent and servers A and B are all accessible on the same Docker network.
*   **Configure `claude_desktop_config.json`:**

    *   Locate your `claude_desktop_config.json` file (the path depends on your operating system; consult the MCP docs for details).

    *   Add configurations for your *gateway-agent* server under the `mcpServers` key. Since your gateway agent now uses HTTP/SSE, you will need to specify the URL accordingly.

        ```json
        {
          "mcpServers": {
            "gateway-agent": {
              "url": "http://localhost:8000/mcp/v1" // Replace with gateway agent url
            },
            "server-a": {
              "url": "http://localhost:5000/mcp/v1" // Replace with Server A url
            },
              "server-b": {
              "url": "http://localhost:5001/mcp/v1" // Replace with Server B url
            }
          }
        }
        ```

        Make sure the port numbers match the ports your servers are listening on.  Replace `/mcp/v1` with the actual endpoint if it's different.  Make sure to add server B analogous to server A, and start it on a different port. 

*   **Restart Claude Desktop:** For the changes in your `claude_desktop_config.json` file to take effect, you need to restart Claude Desktop.

Now you should be able to interact with your gateway agent via Claude's slash commands or other UI elements provided by Claude Desktop to use MCP tools. You can test the routing by entering queries that should be directed to different servers.

With these steps, you should be able to run your MCP project, inspect server communications with the Inspector, and integrate your gateway agent with Claude Desktop! Let me know if you encounter any issues, and I'll help troubleshoot.
