first_string, last_string = input().split()
total_sum = 0

if len(first_string) > len(last_string):
    for index in range(len(last_string)):
        total_sum += ord(first_string[index]) * ord(last_string[index])

    for index in range(len(last_string), len(first_string)):
        total_sum += ord(first_string[index])

elif len(last_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(last_string[index])

    for index in range(len(first_string), len(last_string)):
        total_sum += ord(last_string[index])

else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(last_string[index])

print(total_sum)
