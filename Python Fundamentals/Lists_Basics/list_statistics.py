number = int(input())

positive_numbers = []
negative_numbers = []

for num in range(number):
    current_number = int(input())
    if current_number < 0:
        negative_numbers.append(current_number)
    elif current_number >= 0:
        positive_numbers.append(current_number)
positive_numbers_count = len(positive_numbers)
negative_numbers_sum = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {positive_numbers_count}")
print(f"Sum of negatives: {negative_numbers_sum}")
