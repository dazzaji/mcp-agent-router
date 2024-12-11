# mcp-hello

This is a primative multi-agent modular initialization capability test prototype of Model Context Protocol.  My test project will have multiple servers and clients.  They will operate in a modular way, the first will create a markdown file based on adding user input text to a content template and saving the file to root directory.  The second will ingest that file and add more info to it then save the updated version to the root.  The alt A third will likewise ingest the output of the second and add still more content and export the third version of the file to the root.  The alt B third server alternatively could take another action.  Treat each of these three like back boxes in the sense that they will not share code or components but we will pretend they are running on different technologies to preserve the modular approach and we will for convenience be able to do things like share a virtual environment and requirements for this first test.  We work in VS Code on my mac.  

The second server will be a decider and will choose which is the best next server.


[include all documentation for MCP] 