from math import pi

figure = input()

if figure == 'square':
    a = float(input())
    print(f'{(a * a):.03f}')
elif figure == 'circle':
    a = float(input())
    print(f'{(pi * a * a):.03f}')


if figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{(a * b):.03f}')
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    print(f'{(a * b / 2):.03f}')
