animal_type = input()

if animal_type == 'dog':
    print('mammal')
elif animal_type == 'snake' or animal_type == 'tortoise' or animal_type == 'crocodile':
    print('reptile')
else:
    print('unknown')