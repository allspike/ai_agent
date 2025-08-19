def get_files_info(working_directory, directory="."):
    if directory.startswith(".."):
        raise Exception(f"Error: Cannot list '{directory}'as it is outside the permitted workign directory)
    full_path  = os.path.join(working_directory, directory)
    absolute = os.path.abspath(full_path)
