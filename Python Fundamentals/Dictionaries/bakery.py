food_and_quantities = input().split()
new_items = {}
for index in range(0, len(food_and_quantities), 2):
    key = food_and_quantities[index]
    value = int(food_and_quantities[index + 1])
    new_items[key] = value

print(new_items)
