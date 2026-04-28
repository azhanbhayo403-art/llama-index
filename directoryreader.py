from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
import sys

load_dotenv()

def main(path: str) -> None:
    # Load documents from a local folder
    documents = SimpleDirectoryReader(path).load_data()

    # Build index
    index = VectorStoreIndex.from_documents(documents)

    # Create a query engine
    query_engine = index.as_query_engine()

    # Ask a question
    response = query_engine.query("When was Apple iPhone invented?")
    print(response)

if __name__ == "__main__":
    main(path=r"D:\LLma\data")
