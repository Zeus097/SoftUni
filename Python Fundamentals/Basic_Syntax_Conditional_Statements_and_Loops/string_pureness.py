number = int(input())
current_string = False

for _ in range(number):
    string = input()
    for char in string:
        if char != "," and char != "." and char != "_":
            current_string = True
        else:
            current_string = False
            break
    if current_string is True:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
