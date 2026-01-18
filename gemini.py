import os
from google import genai

from dotenv import load_dotenv

load_dotenv()  

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

client = genai.Client(api_key=API_KEY)

CHARACTERS = [
    "Eleven", "Mike", "Dustin", "Lucas",
    "Will", "Max", "Steve", "Hopper", "Robin"
]

def get_character(qa_pairs):
    formatted = "\n".join(f"Q: {q}\nA: {a}" for q, a in qa_pairs)

    prompt = f"""
You are a personality classifier.

Based on the quiz questions and the user's selected answers,
assign EXACTLY ONE Stranger Things character.

Rules:
- Choose only ONE character
- Choose only from: {', '.join(CHARACTERS)}
- Return ONLY the character name
- No explanation

Quiz responses:
{formatted}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
