free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
free_space_left = True
box_size = free_space_width * free_space_length * free_space_height
command = input()

while command != "Done":
    current_box_number = int(command)
    box_size -= current_box_number

    if box_size < 0:
        free_space_left = False
        break

    command = input()

if free_space_left:
    print(f"{box_size} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(box_size)} Cubic meters more.")