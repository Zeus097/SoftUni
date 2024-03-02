student_information = {}
command = input()

while ":" in command:
    info = command.split(":")

    student_name, student_id, course_name = info[0], info[1], info[2]

    if course_name not in student_information:
        student_information[course_name] = {}
    student_information[course_name][student_name] = student_id
    command = input()

course_name = " ".join(command.split("_"))

for key, value in student_information.items():
    if course_name in key:
        for nested_key, nested_value in value.items():
            print(f"{nested_key} - {nested_value}")
