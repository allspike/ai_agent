import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

def main():
    load_dotenv()
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    args = sys.argv[1:]
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

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents = messages, config=types.GenerateContentConfig(system_instruction=system_prompt))
    if "--verbose" in args:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
        print('Response:')
    print(response.text)

if __name__ == "__main__":
    main()
