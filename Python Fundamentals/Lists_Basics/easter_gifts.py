gifts = input().split()
command = input()

while command != "No Money":
    tokens = command.split()
    if tokens[0] == "OutOfStock":
        out_of_stock_gift = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == out_of_stock_gift:
                gifts[i] = "None"
    elif tokens[0] == "Required":
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = tokens[1]
    elif tokens[0] == "JustInCase":
        gifts[-1] = tokens[1]

    command = input()

result = [gift for gift in gifts if gift != "None"]
print(" ".join(result))
