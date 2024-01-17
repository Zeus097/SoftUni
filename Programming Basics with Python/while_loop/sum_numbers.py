number = int(input())
sum = 0

while True:
    extra_number = int(input())
    sum += extra_number
    if sum >= number:
        print(sum)
        break