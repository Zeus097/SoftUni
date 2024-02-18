initial_energy = int(input())
command = input()
won_battles_counter = 0
out_of_energy = False

while True:
    if command == "End of battle":
        break

    distance = int(command)
    if initial_energy < distance:
        out_of_energy = True
        break

    initial_energy -= distance
    won_battles_counter += 1
    if won_battles_counter % 3 == 0:
        initial_energy += won_battles_counter

    command = input()

if out_of_energy:
    print(f"Not enough energy! Game ends with {won_battles_counter} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}")
