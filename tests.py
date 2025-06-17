# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

print("-" * 16)
print("Test 1:")
print(get_files_info("calculator", "."))
print("-" * 16)
print("Test 2:")
print(get_files_info("calculator", "pkg"))
print("-" * 16)
print("Test 3:")
print(get_files_info("calculator", "/bin"))
print("-" * 16)
print("Test 4:")
print(get_files_info("calculator", "../"))