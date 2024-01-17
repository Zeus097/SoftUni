budget = float(input())
flour_price_per_kg = float(input())
eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg * 1.25
milk_quantity_price_needed = milk_price_per_liter / 4

bread_cost = flour_price_per_kg + eggs_price_per_pack + milk_quantity_price_needed

number_of_breads = 0
bread_counter = 0
colored_eggs = 0

while budget > 0 and colored_eggs >= 0:
    bread_counter += 1

    if budget <= bread_cost:
        break
    if budget < 0:
        break

    number_of_breads += 1
    colored_eggs += 3
    budget -= bread_cost

    if bread_counter % 3 == 0:
        colored_eggs -= number_of_breads - 2
print(f"You made {number_of_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
