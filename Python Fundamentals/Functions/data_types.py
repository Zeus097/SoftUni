def data_types(command, num_as_string):
    if command == "int":
        return int(num_as_string) * 2
    elif command == "real":
        return f"{(float(num_as_string) * 1.5):.2f}"
    elif command == "string":
        return "$" + num_as_string + "$"

string, number_as_string = input(), input()
print(data_types(string, number_as_string))
