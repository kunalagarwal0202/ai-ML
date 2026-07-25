
from openai import OpenAI
import os

base_url = "http://localhost:11434/v1"
model_name = "gemma3:270m"
user_prompt = "what is todays weather"


def main():
    client = OpenAI(
        api_key="chatollama",
        base_url=base_url,
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": user_prompt}],
    )
    print(response.choices[0].message.content)

main()
  