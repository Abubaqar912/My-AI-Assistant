from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("AI ASSISTANT STARTING...")
print("Type 'exit' to quit.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("ASSISTANT: Goodbye!")
        break
    
    response = client.responses.create(
        model="gpt-5-mini",
        input=user
    )

    print("Assisttant", response.output_text)
