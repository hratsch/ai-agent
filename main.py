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
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

- Read file contents

- Execute Python files with optional arguments

- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

messages = [
    types.Content(role="user", parts=[types.Part(text=content)])
]



###
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
#
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists files information within the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to list the file information, relative to the working directory.",
            ),
        },
    ),
)
#
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to execute, relative to the working directory.",
            ),
        },
    ),
)
#
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The data to which is written or overwritten to the file",
            ),
        },
    ),
)
###

###
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)
###

###
question = client.models.generate_content(
    model=g_model, 
    contents=messages, 
    config=types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt
    )
)
###

# function
def call_function(function_call_part, verbose=False):
    if function_call_part:
        for parts in function_call_part:
            if verbose:
                print(f"Calling function: {parts.name}({parts.args})")
            
            print(f" - Calling function: {parts.name}")
        

if verbose_enabled:
    print(f"User prompt: {content}")
    print(f"Prompt tokens: {question.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {question.usage_metadata.candidates_token_count}")


if question.function_calls:
    for calls in question.function_calls:
        print(f"Calling function: {calls.name}({calls.args})")
else:
    print(question.text)