students_number = int(input())
average_grade = 0
fail_counter = 0
third_counter = 0
fourth_counter = 0
top_counter = 0

failed_students_percentage = 0
third_counter_percentage = 0
fourth_counter_percentage = 0
top_counter_percentage = 0

for statistic in range(students_number):
    student_grade_exam = float(input())
    if 2.00 <= student_grade_exam <= 2.99:
        fail_counter += 1
    elif 3.00 <= student_grade_exam <= 3.99:
        third_counter += 1
    elif 4.00 <= student_grade_exam <= 4.99:
        fourth_counter += 1
    else:
        top_counter += 1
    failed_students_percentage = fail_counter / students_number * 100
    third_counter_percentage = third_counter / students_number * 100
    fourth_counter_percentage = fourth_counter / students_number * 100
    top_counter_percentage = top_counter / students_number * 100
    average_grade += student_grade_exam / students_number

print(f"Top students: {top_counter_percentage:.02f}%")
print(f"Between 4.00 and 4.99: {fourth_counter_percentage:.02f}%")
print(f"Between 3.00 and 3.99: {third_counter_percentage:.02f}%")
print(f"Fail: {failed_students_percentage:.02f}%")
print(f"Average: {average_grade:.02f}")