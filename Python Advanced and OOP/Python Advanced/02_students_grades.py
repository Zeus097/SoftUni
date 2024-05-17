students_number = int(input())
students_colection = {}
for _ in range(students_number):
    command = input().split()
    student_name, student_grade = command[0], float(command[1])

    if student_name not in students_colection:
        students_colection[student_name] = []
    students_colection[student_name].append(student_grade)

for student_name, student_grades in students_colection.items():
    average_grade = sum(student_grades) / len(student_grades)
    grade = [f"{current_grade:.2f}" for current_grade in student_grades]

    print(f"{student_name} -> {' '.join(grade)} (avg: {average_grade:.2f})")
