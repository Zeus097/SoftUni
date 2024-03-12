path_of_file = input().split("\\")
file_name_and_extension = path_of_file[-1]
file_name, file_extension = file_name_and_extension.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
