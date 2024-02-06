first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
total_hours = 0

total_efficiency = (first_employee_efficiency +
                    second_employee_efficiency +
                    third_employee_efficiency)

while True:
    if student_count <= 0:
        break
    total_hours += 1
    if total_hours % 4 == 0:
        continue

    if total_efficiency >= student_count:
        break
    else:
        student_count -= total_efficiency


print(f"Time needed: {total_hours}h.")
