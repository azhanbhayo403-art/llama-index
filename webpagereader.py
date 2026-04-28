
from llama_index.readers import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
import os
from dotenv import load_dotenv

load_dotenv()

def main(url : str)->None:
    document = SimpleWebPageReader(html_to_text = True).load_data(urls = [url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    respone = query_engine.query("when was apple iphone invented?")
    print(respone)

if __name__=="__main__":
    main(url="https://en.wikipedia.org/wiki/IPhone")
    