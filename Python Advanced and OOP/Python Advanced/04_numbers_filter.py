def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [int(x) for x in kwargs[key] if x % 2 == 0]
        elif key == "odd":
            kwargs[key] = [int(x) for x in kwargs[key] if x % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))

# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
