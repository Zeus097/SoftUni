numbers = list(map(int, input().split()))
numbers.sort()
numbers.reverse()
sum_numbers = sum(numbers)
average_value = sum_numbers // len(numbers)
top_numbers = []
counter = 0

for current_number in numbers:
    counter += 1

    if current_number > average_value:
        top_numbers.append(current_number)
    if counter == 5:
        break

if len(top_numbers) == 0:
    print("No")
else:
    print(" ".join(map(str, top_numbers)))
