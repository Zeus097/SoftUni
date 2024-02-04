def loading_bar(num):
    percent = int(num // 10) * "%"
    point_mark = int(100 - num) // 10 * "."
    if num % 10 == 0 and num != 100:
        print(f"{num}% [{percent}{point_mark}]")
        print("Still loading...")
    elif num == 100:
        print(f"{num}% Complete!")
        print(f"[{percent}]")

number = int(input())
loading_bar(number)
