def fill_the_box(height, length, width, *args):
    cub_size = height * length * width
    filled_space = 0
    for current_cube in args:
        if current_cube == "Finish":
            break
        filled_space += current_cube

    difference = abs(cub_size - filled_space)
    if cub_size > filled_space:
        return f"There is free space in the box. You could put {difference} more cubes."
    return f"No more free space! You have {difference} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
