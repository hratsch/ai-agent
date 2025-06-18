import os
import subprocess

def run_python_file(working_directory, file_path):

    # vars
    target_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(target_path).startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.isfile(target_path):
        return f"Error: File \"{file_path}\" not found."

    if not target_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."

    try:
        run_file = subprocess.run(['python3', target_path], capture_output=True, text=True, timeout=30)

        if run_file.stdout == "" and run_file.stderr == "":
            return "No output produced"

        if run_file.returncode != 0:
            return f"STDOUT: {run_file.stdout} \n STDERR: {run_file.stderr} \n Process exited with code {run_file.returncode}"

        return f"STDOUT: {run_file.stdout} \n STDERR: {run_file.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"