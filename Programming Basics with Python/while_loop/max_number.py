from sys import maxsize
data = input()
max = - maxsize

while True:
    if data == "Stop":
        break
    number = int(data)

    if number > max:
        max = number
    data = input()

print(max)