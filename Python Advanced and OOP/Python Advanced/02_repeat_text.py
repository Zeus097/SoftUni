text = input()

while True:
    try:
        times = int(input())
        print(times * text)
        break
    except ValueError:
        print("Variable times must be an integer")
