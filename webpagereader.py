#from llama_index.llms import OpenAI
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex

import llama_index
import os
from dotenv import load_dotenv


load_dotenv()

#creating a method 
#where the type of the url is a string and it wont return anything
def main(url: str)-> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine= index.as_query_engine()
    response = query_engine.query("what is the history of genai?")
    print(response)


if __name__=="__main__":
    main(url="https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786")
