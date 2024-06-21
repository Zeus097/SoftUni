def softuni_students(*args, **kwargs):
    result = ""
    collection = {}
    invalid_names = []

    for course_id, username in args:
        if course_id in kwargs:
            course_name = kwargs[course_id]
            collection[username] = course_name
        else:
            invalid_names.append(username)

    sorted_collection = sorted(collection.items())
    sorted_invalid_names = sorted(invalid_names)

    for name, current_course in sorted_collection:
        result += f"*** A student with the username {name} has successfully finished the course {current_course}!\n"

    if invalid_names:
        result += f"!!! Invalid course students: {', '.join(sorted_invalid_names)}\n"

    return result.strip()


# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))
