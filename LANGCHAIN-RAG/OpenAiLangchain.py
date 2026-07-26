
from openai import OpenAI
import os

base_url = "http://localhost:11434/v1"
model_name = "gpt-5"
user_prompt = "what is todays weather"


def main():
    client = OpenAI(
        api_key="Your own key stupid"
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": user_prompt}],
    )
    print(response.choices[0].message.content)

main()
  