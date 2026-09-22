from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables from a .env file if present
load_dotenv()

client = OpenAI()

VECTOR_STORE_NAME = "MEMORIES"

mcp = FastMCP("memories")

# whatever conversation you have with mcp cient can be stored in openai's vector store as a memory so that it can effectively searched for
# and retrieved using RAG's semantic search instead of manually storing locally in a temp file and doing a keyword search on them!

# creates a vector store using openai API to store memories via temp files
def get_or_create_vector_store():
    # Try to find existing vector store, else create
    stores = client.vector_stores.list()
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)

# tool to save memory in openai's vector db via a temp file
@mcp.tool()
def save_memory(memory: str):
    """Save a memory string to the vector store."""
    # Save memory to a temp file for upload
    vector_store = get_or_create_vector_store()

    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as f:
        f.write(memory)
        f.flush()
        client.vector_stores.files.upload_and_poll(
            vector_store_id=vector_store.id,
            file=open(f.name, "rb")
        )
    return {"status": "saved", "vector_store_id": vector_store.id}

# tool to search openai's vector store for the stored memory as text
def search_memory(query: str):
    """Search memories in the vector store and return relevant chunks."""
    vector_store = get_or_create_vector_store()
    results = client.vector_stores.search(
        vector_store_id=vector_store.id,
        query=query
    )

    content_texts = [
        content.texts
        for item in results.data
        for content in item.content
        if content.type == "text"
    ]

    return {"results": content_texts}

if __name__ == "__main__":
    mcp.run()