from math import ceil

number_of_people = int(input())
capacity_of_elevator = int(input())

total_elevator_courses = ceil(number_of_people / capacity_of_elevator)
print(total_elevator_courses)
