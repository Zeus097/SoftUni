def concatenate(*args, **kwargs):
    string = ''.join(args)
    for key, value in kwargs.items():
        string = string.replace(key, value) if key in string else string

    return string


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
#
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
