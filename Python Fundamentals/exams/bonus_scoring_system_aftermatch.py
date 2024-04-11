from math import ceil


def attendances_calculation(students, lectures, bonus):
    max_bonus = 0
    student_attend = 0
    for current_student in range(students):
        current_student_attendance = int(input())
        total_bonus = current_student_attendance / lectures * (5 + bonus)
        if total_bonus >= max_bonus:
            max_bonus = total_bonus
            student_attend = current_student_attendance

    return f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {student_attend} lectures."


number_of_students = int(input())
total_lectures_number = int(input())
additional_bonus = int(input())
final_result = attendances_calculation(number_of_students, total_lectures_number, additional_bonus)
print(final_result)
