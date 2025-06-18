# from subdirectory.filename import function_name
from functions.run_python_file import run_python_file

print("-" * 16)
print("Test 1:")
print(run_python_file("calculator", "main.js"))
print("-" * 16)
print("Test 2:")
print(run_python_file("calculator", "tests.py"))
print("-" * 16)
print("Test 3:")
print(run_python_file("calculator", "../main.py"))
print("-" * 16)
print("Test 4:")
print(run_python_file("calculator", "nonexistent.py"))