from math import floor

def closest_to_center():

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    distance1 = (x1**2 + y1**2)**0.5
    distance2 = (x2**2 + y2**2)**0.5

    if distance1 <= distance2:
        closest_point = (x1, y1)
    else:
        closest_point = (x2, y2)

    formatted_coordinates = f"({floor(closest_point[0])}, {floor(closest_point[1])})"
    print(formatted_coordinates)

closest_to_center()
