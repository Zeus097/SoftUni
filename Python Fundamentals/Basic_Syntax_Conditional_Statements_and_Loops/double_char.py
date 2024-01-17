while True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for char in string:
        new_string = char * 2
        print(new_string, end="")
    print()
