bad_grades = int(input())
grades_counter = 0
bad_grades_counter = 0
grades_sum = 0
last_task_name = ""
enough_bad_grades = False
average_score = 0
task_name = input()

while task_name != "Enough":
    grades = int(input())
    grades_counter += 1
    grades_sum += grades
    average_score = abs(grades_sum / grades_counter)
    last_task_name = task_name

    if grades <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades:
            enough_bad_grades = True
            break

    task_name = input()

if enough_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {grades_counter}")
    print(f"Last problem: {last_task_name}")



