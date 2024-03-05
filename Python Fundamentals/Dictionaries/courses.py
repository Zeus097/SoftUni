courses = {}

while True:
    command = input()
    if command == "end":
        break

    information = command.split(" : ")

    course_name = information[0]
    registered_student = information[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(registered_student)

for course_name, student_name in courses.items():
    print(f"{course_name}: {len(student_name)}")
    for student in student_name:
        print(f"-- {''.join(student)}")
