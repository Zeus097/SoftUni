from math import pi

number = float(input())
circle_area = pi * (number ** 2)
circle_parameter = 2 * pi * number


print(f"{circle_area:.2f}")
print(f"{circle_parameter:.2f}")