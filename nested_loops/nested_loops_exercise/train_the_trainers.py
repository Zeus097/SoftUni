jury_number = int(input())
final_grade = 0
presentation_number = 0
command = input()
while command != "Finish":
    presentation_name = command
    presentation_number += 1
    current_presentation_grade = 0
    for presentation_grade in range(jury_number):
        current_grade = float(input())
        current_presentation_grade += current_grade
    average_grade = current_presentation_grade / jury_number
    print(f"{presentation_name} - {average_grade:.2f}.")
    final_grade += average_grade
    command = input()
final_average_grade = final_grade / presentation_number
print(f"Student's final assessment is {final_average_grade:.2f}.")