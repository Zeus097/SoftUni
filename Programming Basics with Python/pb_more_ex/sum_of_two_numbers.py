start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination_found = False
combination_count = 0
for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        combination_count += 1
        if num1 + num2 == magic_number:
            combination_found = True
            print(f"Combination N:{combination_count} ({num1} + {num2} = {magic_number})")
            break
    if combination_found:
        break

if not combination_found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
