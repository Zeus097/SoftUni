from math import floor

def closer_point(arg1, arg2, arg3, arg4):
    one = arg1 + arg2
    two = arg3 + arg4
    if one > two:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif one < two:
        if abs(x3) + abs(y3) > abs(x4) + abs(y4):
            return f"({x4}, {y4})({x3}, {y3})"
        else:
            return f"({x3}, {y3})({x4}, {y4})"
    else:
        if abs(x3) + abs(y3) > abs(x4) + abs(y4):
            return f"({x4}, {y4})({x3}, {y3})"
        else:
            return f"({x3}, {y3})({x4}, {y4})"

x1, x2 = floor(float(input())), floor(float(input()))
y1, y2 = floor(float(input())), floor(float(input()))
x3, y3 = floor(float(input())), floor(float(input()))
x4, y4 = floor(float(input())), floor(float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))

sum_z = floor(abs(x3) + abs(y3))
sum_v = floor(abs(x4) + abs(y4))

print(closer_point(sum_x, sum_y, sum_z, sum_v))
