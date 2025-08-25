import os

# funciton to write to a file with specificed content
def write_file(working_directory, file_path, content):
    # gain the absolute file path
    absolute = os.path.abspath(os.path.join(working_directory, file_path))
    # obtain the file_directory 
    file_directory = os.path.dirname(absolute)
    # if the file directory is outside of the permitted working directory, return an error message
    if not file_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        # if the path to the file directory exists, open the file and write the contents
        if os.path.exists(file_directory):
            with open(absolute, "w") as f:
                f.write(content)
        # otherwise create all the directories recursively and then open the file
        else:
            os.makedirs(file_directory, exist_ok=True)
            with open(absolute, "w") as f:
                f.write(content)
        return f'Successfully wrote to "{file_path} ({len(content)} characters written)'
            
    # return any other error
    except Exception as e:
        return f'Error: {e}'
