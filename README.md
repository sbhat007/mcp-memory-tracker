# mcp-memory-tracker
Install this mcp server by adding below json to your mcp config file
This is possible as chess follow the required folder structure 

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

There is one more server.py at the root which hosts tools to store chat interactions as memories and later search in them. However, this would require openAI key