nylon = int(input())
paint = int(input())
thinner = int(input())
hours_needed = int(input())
nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint*0.1)) * 14.50
thinner_price = thinner * 5.00
nylon_bag_price = 0.40
price_for_materials = nylon_price + paint_price + thinner_price + nylon_bag_price
workers_payment = price_for_materials * 0.3 * hours_needed
totall_price = price_for_materials + workers_payment

print(totall_price)
