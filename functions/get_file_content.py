import os
from google.genai import types

def get_file_content(working_directory, file_path):
    absolute = os.path.abspath(os.path.join(working_directory, file_path))
    if not absolute.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHARS = 10000
    trunc_message = f'[...File "{file_path}" truncated at 10000 characters]'
    try:
        with open(absolute, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                f.seek(0)
                trunc_content = f.read(MAX_CHARS)
                return trunc_content + '\n' +  trunc_message
            else:
                return file_content_string
    except Exception as e:
        return f'Error: {e}'
            
            

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Lists file content in the specificed directory, constrained to the working working_directory. If the file is over 10,000 characters, then truncate the contents size to 10000",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path within the working directory.",
                    ),
                },
            ),
        )
