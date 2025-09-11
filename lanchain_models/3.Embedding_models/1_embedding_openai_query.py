import os
from langchain_openai import OpenAIEmbeddings


os.environ["OPENAI_API_KEY"] = "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"



embedding = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32,  # or "text-embedding-3-large"
    )

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))