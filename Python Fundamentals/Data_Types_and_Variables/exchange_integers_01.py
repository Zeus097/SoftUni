number_one = int(input())
number_two = int(input())

change_complete = False

while True:
    print("Before:")
    print(f"a = {number_one}")
    print(f"b = {number_two}")

    change_complete = True

    print("After:")
    print(f"a = {number_two}")
    print(f"b = {number_one}")

    if change_complete:
        break
