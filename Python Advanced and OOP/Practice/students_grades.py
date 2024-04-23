students_number = int(input())
students = {}

for i in range(students_number):
    student_name, student_grade = input().split()
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(student_grade))

for student, grades in students.items():
    formatted_grade = ' '.join([f'{grade:.2f}' for grade in grades])
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {formatted_grade} (avg: {average_grade:.2f})")
