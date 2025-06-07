from openai import AzureOpenAI

endpoint = "https://ai-gpt-instance.openai.azure.com/"
model_name = "gpt-35-turbo"
deployment = "gpt-35-turbo-default"

subscription_key = "748f28e0fdb44d919a2f1bc89004d444"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)
system_message = "you are responsible for providing task options for secondary students"

response = client.chat.completions.create(
    model=deployment,
    temperature=0.6,
    max_tokens=400,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": "Suggest two activity options from"}
    ]
)
# print(response)

content = response.choices[0].message.content
print(content)