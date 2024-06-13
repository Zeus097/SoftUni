import os


def directory_traversing(dir_name, extension_collection, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            extension_collection[extension] = extension_collection.get(extension, []) + [file_name]
        elif os.path.isdir(file) and not first_level:
            directory_traversing(file, extension_collection, first_level=True)


def sorting_information(collected_extensions):
    for key in collected_extensions:
        collected_extensions[key] = sorted(collected_extensions[key])
    sorted_extensions = dict(sorted(collected_extensions.items(), key=lambda x: x[0]))
    return sorted_extensions


def save_info(data):
    with open('report.txt', 'w') as file:
        for file_type, file_name in data.items():
            file.write(f".{file_type}\n- - - {'\n- - - '.join(file_name)}\n")


def main():
    extensions = {}
    while True:
        directory = input()
        try:
            directory_traversing(directory, extensions)
            break
        except FileNotFoundError:
            print('No such file or directory found!')

    sorted_information = sorting_information(extensions)
    save_info(sorted_information)


if __name__ == '__main__':
    main()
