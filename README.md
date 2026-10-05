# mcp-memory-tracker
1. Install this mcp server by adding below json to your mcp config file
This is possible as chess follows the required folder structure 

    ~~~
    "Chess": {
          "command": "uvx",
          "args": [
            "--from",
            "git+https://github.com/sbhat007/mcp-memory-tracker.git",
            "chess"
          ]
        }
    ~~~

2. There is one more server.py at the root which hosts tools to store chat interactions as memories and later search in them. However, this would require openAI key

3. Finally we have client.py which when run accepts user input, passes onto openAI mcp client specifying the tools that can be used. 
One of the tools we have is storing and searching conversations from openAI vector db which openAI will automatically search before making any call tools to get relevant info 
4. chat_ui.py - Sample chatbot developed in python 