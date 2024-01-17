number = int(input())
arithmetic = 0
total_sum = 0

for _ in range(number):
    current_number = float(input())
    total_sum += current_number
    arithmetic = total_sum / number

print(f"{arithmetic:.02f}")