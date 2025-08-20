import os
def get_files_info(working_directory, directory="."):
 
    full_path = os.path.join(working_directory, directory)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return  f'Error: Cannot list "{directory}"as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return  f'Error: "{directory}" is not a directory'
    result = ""
    try:
        for item in os.listdir(full_path):
            new_path = os.path.join(full_path, item)
            result += "- " + f"{item}: file_size={os.path.getsize(new_path)}, is_dir={os.path.isdir(new_path)}" + "\n"
        return result
    except Exception as e:
        return f"Error: {e}"
