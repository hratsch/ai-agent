import os

def get_files_info(working_directory, directory=None):

    if directory == None:
        directory = "."

    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(directory):
        return f"Error: '{directory}' is not a directory"
        

    # vars
    ls_dir = os.listdir(os.path.join(working_directory, directory))

    # empty list
    reveal_items = []
    
    for items in ls_dir:
        full_path = os.path.join(directory, items)
        # reveal_items.append(each_item)
        reveal_items.append(f"- {items}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
    return "\n".join(reveal_items)