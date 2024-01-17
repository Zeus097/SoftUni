floor_number = int(input())
flat_number = int(input())
flat_name = ""

for floor in range(floor_number, 0, -1):
    for flat in range(flat_number):

        if floor_number == floor:
            flat_name = f"L{floor}{flat}"

        elif floor % 2 == 0:
            flat_name = f"O{floor}{flat}"

        elif floor % 2 != 0:
            flat_name = f"A{floor}{flat}"

        print(flat_name, end=" ")

    print()