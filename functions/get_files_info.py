import os

def get_files_info(working_directory, directory=None):

    if directory == None:
        directory = "."

    # vars
    target_dir = os.path.join(working_directory, directory)

    if not os.path.abspath(target_dir).startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(target_dir):
        return f"Error: '{directory}' is not a directory"

    # after safety checks and to catch any errors
    try:
        ls_dir = os.listdir(target_dir)
    except Exception as e:
        return f"Error: {str(e)}"

    # empty list
    reveal_items = []
    
    for items in ls_dir:
        full_path = os.path.join(target_dir, items)
        # catch any possible errors
        try:
            reveal_items.append(f"- {items}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
        except Exception as e:
            return f"Error: {str(e)}"
    return "\n".join(reveal_items)