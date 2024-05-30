def sorting_cheeses(**kwargs):
    sorted_cheeses = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''
    for key, value in sorted_cheeses.items():
        result += key + '\n'
        sorted_value = sorted(value, reverse=True)
        for item in sorted_value:
            result += str(item) + '\n'
    return result


# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
