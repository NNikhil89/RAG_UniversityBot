from groq import Groq

client = Groq(api_key="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")
available_models = client.models.list()
for
print(available_models)
