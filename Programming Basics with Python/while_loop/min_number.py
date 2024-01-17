from sys import maxsize

data = input()
min = maxsize

while True:
    if data == "Stop":
        break

    number = int(data)

    if number < min:
        min = number
    data = input()

print(min)
