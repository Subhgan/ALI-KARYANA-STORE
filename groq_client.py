import os
from dotenv import load_dotenv
from groq import Groq

# Load the API key from our .env file
load_dotenv()

# Connect to Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Select the AI model
GROQ_MODEL = "openai/gpt-oss-120b"


def get_groq_response(messages):
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=0.5
    )

    return response.choices[0].message.content