number = float(input())
current_number = 0

while True:
    current_number = number * 2
    print(f"Result: {current_number:.02f}")
    number = float(input())
    if number < 0:
        print("Negative number!")
        break