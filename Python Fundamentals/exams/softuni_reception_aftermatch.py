def needed_time(employees_efficiency, number_of_students):
    working_hour = 0
    while number_of_students > 0:
        working_hour += 1
        if working_hour % 4 == 0:
            continue
        number_of_students -= employees_efficiency
    return working_hour


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
time = needed_time(total_efficiency, students_count)

print(f"Time needed: {time}h.")
