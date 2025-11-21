import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("BASE_KEY_OPENROUTER"))

messages = [
    {"role": "system", "content":"You are free creative assistant freely about topics and ideas."},
    {"role": "user", "content":"Give me 5 ideas, think about various topics in IT field and the things that can be done. Like micro oppourtunities or things that can be done and should be done and needed but nobody does. Small things. Different and New."}
]

respons = client.chat.completions.create(
    model="x-ai/grok-4.1-fast:free",
    messages=messages,
    temperature=1.5
)

print(respons.choices[0].message.content)

