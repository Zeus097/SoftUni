# 08. Equal Pairs

number_counter = int(input())

value = 0
diff = 0
no = False

for num in range(number_counter):
    number_one = int(input())
    number_two = int(input())
    if number_one + number_two != value and value != 0:
        diff = abs(number_one + number_two - value)
        value = number_one + number_two
        no = True
    else:
        value = number_one + number_two

if no:
    print(f"No, maxdiff={diff}")
else:
    print(f"Yes, value={value}")