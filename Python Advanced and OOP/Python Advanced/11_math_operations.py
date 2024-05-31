def math_operations(*args, **kwargs):

    for index in range(len(args)):
        if index % 4 == 0:
            kwargs['a'] += args[index]
        elif index % 4 == 1:
            kwargs['s'] -= args[index]
        elif index % 4 == 2 if args[index] != 0 else 0:
            kwargs['d'] /= args[index]
        elif index % 4 == 3:
            kwargs['m'] *= args[index]

    result = dict(sorted(kwargs.items(), key=lambda kwp: (-kwp[1], kwp[0])))
    final_result = ''
    for key, value in result.items():
        final_result += f"{key}: {value:.1f}\n"

    return final_result


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
