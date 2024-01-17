divisor = int(input())
boundary = int(input())
maximum_divisor = 0

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        maximum_divisor += number
        break

print(maximum_divisor)
