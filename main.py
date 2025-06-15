import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# gets .env var
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# create new instance of Gemini client
client = genai.Client(api_key=api_key)



# checks for cli arguements
if len(sys.argv) < 2:
    print("Usage: python3 main.py 'insert your question here...'")
    sys.exit(1)

if "--verbose" in sys.argv:
    verbose_enabled = True
else:
    verbose_enabled = False

g_model = "gemini-2.0-flash-001"
content = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=content)])
]

question = client.models.generate_content(model=g_model, contents=messages)

if verbose_enabled:
    print(f"User prompt: {content}")
    print(f"Prompt tokens: {question.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {question.usage_metadata.candidates_token_count}")

print(question.text)
