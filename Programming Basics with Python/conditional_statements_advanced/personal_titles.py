age = float(input())
gender = input()

if age >= 16 and gender == 'm':
    print('Mr.')
if age < 16 and gender == 'm':
    print('Master')
if age >= 16 and gender == 'f':
    print('Ms.')
if age < 16 and gender == 'f':
    print('Miss')