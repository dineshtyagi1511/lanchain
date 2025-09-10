from langchain_openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

LLm =OpenAI(model="gpt-3.5-turbo-instruct",api_key=api_key)

result =LLm.invoke("What is The capital of india ?")

print(result)
