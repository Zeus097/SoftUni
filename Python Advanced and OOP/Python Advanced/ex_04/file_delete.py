import os

file_path = 'file_to_delete_01.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')
