queue = input()

sheep_in_danger = 0
my_list = queue.split()
if my_list[(len(my_list) - 1)] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    my_list.reverse()
    for list_index in range(len(my_list)):
        if my_list[list_index] == "wolf,":
            sheep_in_danger = list_index
            print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")