box_of_clothes = [int(x) for x in input().split()]
single_rack_capacity = int(input())
needed_racks = 0

while box_of_clothes:
    needed_racks += 1
    current_rack_capacity = single_rack_capacity
    while current_rack_capacity and box_of_clothes:
        if box_of_clothes[-1] <= current_rack_capacity:
            current_rack_capacity -= box_of_clothes.pop()
        else:
            break

print(needed_racks)
