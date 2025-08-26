import os
import subprocess

def run_python_file(working_directory, file_path, fargs=[]):
    # first get the path to the file
    absolute = os.path.abspath(os.path.join(working_directory, file_path))

    # check to make sure that it is within our working directory
    if not absolute.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # if it doesn't exist, return an error
    if not os.path.exists(absolute):
        return f'Error: File "{file_path}" not found.'

    # if the file doesn't end with .py, return an error
    if not absolute.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try: 
        # open the file and store it as an object
        with open(absolute, "r") as f:
        
            # our result string that starts empty
            res_str = ""
            # run the subprocess.run method
            # this produces a Completed Process instance
            result = subprocess.run(args=["python", file_path] + fargs, timeout=30, cwd=os.path.abspath(working_directory), capture_output=True, text=True)
            # if both stdout and stderr are empty exit the function and return the string that says nothing was produced
            if len(result.stdout) == 0 and len(result.stderr) == 0:
                return 'No output produced'
            else:
                # otherwise, build our result string
                res_str += f'STDOUT: {result.stdout}\n STDERR: {result.stderr}'
            # if the return code isn't 0, return an error message with the return codd
            if result.returncode != 0:
                res_str += f'Process exited with code {result.returncode}'
            return res_str
    except Exception as e:
        return f'Error: {e}'
