# from subdirectory.filename import function_name
from functions.get_file_content import get_file_content

print("-" * 16)
print("Test 1:")
print(get_file_content("calculator", "main.py"))
print("-" * 16)
print("Test 2:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("-" * 16)
print("Test 3:")
print(get_file_content("calculator", "/bin/cat"))