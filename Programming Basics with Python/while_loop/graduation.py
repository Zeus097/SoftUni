student_name = input()
grades_counter = 0
years_counter = 0
failed_year_counter = 0

while years_counter < 12:
    current_grade = float(input())

    if current_grade < 4:
        failed_year_counter += 1
        if failed_year_counter > 1:
            excluded_year = years_counter + 1
            print(f"{student_name} has been excluded at {excluded_year} grade")
            break

        continue

    grades_counter += current_grade
    years_counter += 1

else:
    average_grade = grades_counter / years_counter
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
