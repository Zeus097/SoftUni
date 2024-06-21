def gather_credits(credits_needed, *args):
    result = ""
    max_credits = 0
    open_courses = {}
    enrolled_courses = []

    for course_name, course_credits in args:
        open_courses[course_name] = int(course_credits)

    for current_course_name, current_course_credits in open_courses.items():
        if max_credits >= credits_needed:
            break

        enrolled_courses.append(current_course_name)
        max_credits += current_course_credits

    sorted_courses = sorted(enrolled_courses)

    if max_credits >= credits_needed:
        result += f"Enrollment finished! Maximum credits: {max_credits}.\nCourses: {', '.join(sorted_courses)}"
    else:
        difference = abs(max_credits - credits_needed)
        result += f"You need to enroll in more courses! You have to gather {difference} credits more."

    return result


# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
