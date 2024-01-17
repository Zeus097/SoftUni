height = int(input())
wide = int(input())
needed_cake_peace = height * wide
pieces_left = False

while needed_cake_peace > 0:
    text = input()
    if text == "STOP":
        pieces_left = True
        break

    service = int(text)
    needed_cake_peace -= service

    service = int(text)

if pieces_left:
    print(f"{abs(needed_cake_peace)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(needed_cake_peace)} pieces more.")