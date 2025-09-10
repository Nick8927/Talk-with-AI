from openai import OpenAI
from dotenv import load_dotenv
from os import getenv


load_dotenv()
AI_TOKEN = getenv("AI_TOKENv3")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-chat",
  messages=[
    {
      "role": "user",
      "content": "Как дела, мой друг?"
    }
  ]
)
print(completion.choices[0].message.content)