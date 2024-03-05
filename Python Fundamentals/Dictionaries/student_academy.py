number_of_pairs = int(input())
students_information = {}

for i in range(number_of_pairs):
    name = input()
    grade = float(input())

    if name not in students_information:
        students_information[name] = []
    students_information[name].append(grade)

for name, value in students_information.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
