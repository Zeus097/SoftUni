cucle_number = int(input())
even_sum = 0
odd_sum = 0

for number in range(1, cucle_number + 1):
    current_number = int(input())
    if number % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
        diff = abs(even_sum - odd_sum)

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {diff}")