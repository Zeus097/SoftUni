def age_assignment(*args, **kwargs):
    assignments = {}
    for word, age in kwargs.items():
        for name in args:
            if name.startswith(word):
                assignments[name] = age

    sorted_names = dict(sorted(assignments.items()))
    result = ''
    for name, age in sorted_names.items():
        result += f"{name} is {age} years old.\n"

    return result


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
