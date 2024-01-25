number = int(input())

my_list = []

for num in range(number):
    current_number = int(input())
    my_list.append(current_number)

command = input()

filtered_list = []

if command == "even":
    for num in my_list:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == "odd":
    for num in my_list:
        if num % 2 != 0:
            filtered_list.append(num)
elif command == "negative":
    for num in my_list:
        if num < 0:
            filtered_list.append(num)
elif command == "positive":
    for num in my_list:
        if num >= 0:
            filtered_list.append(num)

print(filtered_list)
