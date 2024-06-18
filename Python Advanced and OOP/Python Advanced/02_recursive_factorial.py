def calc_factorial(n):
    if n == 0:
        return 1
    return n * calc_factorial(n-1)


num = int(input())
print(calc_factorial(num))
