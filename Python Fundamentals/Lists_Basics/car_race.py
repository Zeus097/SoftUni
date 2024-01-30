time_index = [int(num) for num in input().split(" ")]
left_car = 0
right_car = 0

middle_index = len(time_index) // 2
middle_element = time_index[middle_index]

for l_time in time_index[0:middle_index]:
    if l_time == 0:
        left_car *= 0.8
    else:
        left_car += l_time

for r_time in time_index[-1:middle_index:-1]:
    if r_time == 0:
        right_car *= 0.8
    else:
        right_car += r_time

if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
else:
    print(f"The winner is right with total time: {right_car:.1f}")
