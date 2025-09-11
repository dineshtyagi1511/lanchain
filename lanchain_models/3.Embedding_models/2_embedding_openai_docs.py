from langchain_openai import OpenAIEmbeddings
import os 

os.environ["OPENAI_API_KEY"] = "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"

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))