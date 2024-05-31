def func_executor(*args):
    elements = []
    for func_name, data in args:
        elements.append(f"{func_name.__name__} - {func_name(*data)}")

    return '\n'.join(elements)


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))
