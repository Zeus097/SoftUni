def upper_rhombus(number):
    for i in range(1, number + 1):
        printing_output(number, i)


def lower_rhombus(number):
    for i in range(number - 1, 0, -1):
        printing_output(number, i)


def rhombus(number):
    upper_rhombus(number)
    lower_rhombus(number)


def printing_output(number, i):
    print(f"{' ' * (number - i)}{'* ' * i}")


n = int(input())
rhombus(n)
