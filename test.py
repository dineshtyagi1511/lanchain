



from openai import OpenAI

client = OpenAI(api_key="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")
print(client.models.list())
