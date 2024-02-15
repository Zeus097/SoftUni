neighbourhood = list(map(int, input().split("@")))
current_index = 0
command = input()

while True:


    if command == "Love!":
        break

    command_line = command.split()
    step = int(command_line[1])

    if step + current_index <= len(neighbourhood) - 1:
        current_index += step
        if neighbourhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighbourhood[current_index] -= 2
            if neighbourhood[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")
    else:
        current_index = 0
        if neighbourhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighbourhood[current_index] -= 2
            if neighbourhood[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")

if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    failed_house = [failed_house for failed_house in neighbourhood if failed_house != 0]
    print(f"Cupid has failed {len(failed_house)} places.")
