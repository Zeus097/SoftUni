height_wall = float(input())
length_wall = float(input())
height_roof = float(input())

side_wall = height_wall * length_wall
window = 1.5 * 1.5
side_walls = (side_wall) * 2 - (window * 2)
back_wall = height_wall * height_wall
entrance = 1.2 * 2
front_and_back_wall = (back_wall * 2) - entrance
total_space_of_walls = side_walls + front_and_back_wall
green_paint = total_space_of_walls / 3.4

roof_side_walls = (height_wall * length_wall) * 2
roof_front_and_back_wall = (height_wall * height_roof / 2) * 2
total_roof_space = roof_side_walls + roof_front_and_back_wall
red_paint = total_roof_space / 4.3


print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")