number = int(input())

if number < 2:
    result = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            result = False
            break
    else:
        result = True

print(result)
