import os
import sys

from dotenv import load_dotenv

from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content 
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

def call_function(function_call_part, verbose=False):
    func_dict = {
            "get_files_info": get_files_info,
            "get_file_content": get_file_content,
            "run_python_file": run_python_file,
            "write_file": write_file,
            }
    if function_call_part.name not in func_dict:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                        )
                    ],
                )
        
    kwargs = dict(function_call_part.args)
    kwargs["working_directory"] = "./calculator/pkg"


    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        
    else:
        print(f" - Calling function: {function_call_part.name}")
    try:
        func = func_dict[function_call_part.name]
        function_result = func(**kwargs)
    except Exception as e:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"{e}"},
                        )
                    ],
                )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result}
                )
            ]
        )

    

def main():
    load_dotenv()
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """ 
    args = sys.argv[1:]
    available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info,
                schema_run_python_file,
                schema_write_file,
                schema_get_file_content,
                ]
            )
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('\nExample: python main.py "How do I build a calculator app?"')
    
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    counter = 0
    while counter < 20:
        try:
            response = client.models.generate_content(model="gemini-2.0-flash-001", contents = messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
        except Exception as e:
            print(f'Error: {e}')
        counter += 1
       
        verbose = False
        if "--verbose" in args:
            verbose = True
            print(f'User prompt: {user_prompt}')
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
            print('Response:')
        found_call = False
        for candidate in response.candidates:
            if not getattr(candidate, "content", None):
                continue
            messages.append(candidate.content)
            parts = getattr(candidate.content, "parts", None)
            if not parts:
                continue
            for part in parts:
                try:
                    fc = getattr(part, "function_call", None)
                    if not fc:
                       continue 
                    found_call = True
                    result = call_function(fc, verbose)
                    tool_part = result.parts[0].function_response
                    messages.append(
                            types.Content(
                                role="user",
                                parts = [
                                    types.Part.from_function_response(
                                        name=tool_part.name,
                                        response=tool_part.response,
                                        )
                                    ],
                                )
                            )
                except Exception as e:
                    print(f"Fatal Error! {e}")
        if not found_call and response.text:
            print("Final Response:")
            print(response.text)
            break
if __name__ == "__main__":
    main()
