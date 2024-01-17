product_type = input()
city = input()
quality = float(input())
product_number = 0

if city == 'Sofia':
    if product_type == 'coffee':
        product_number = quality * 0.50
    if product_type == 'water':
        product_number = quality * 0.80
    if product_type == 'beer':
        product_number = quality * 1.20
    if product_type == 'sweets':
        product_number = quality * 1.45
    if product_type == 'peanuts':
        product_number = quality * 1.60

if city == 'Plovdiv':
    if product_type == 'coffee':
        product_number = quality * 0.40
    if product_type == 'water':
        product_number = quality * 0.70
    if product_type == 'beer':
        product_number = quality * 1.15
    if product_type == 'sweets':
        product_number = quality * 1.30
    if product_type == 'peanuts':
        product_number = quality * 1.50

if city == 'Varna':
    if product_type == 'coffee':
        product_number = quality * 0.45
    if product_type == 'water':
        product_number = quality * 0.70
    if product_type == 'beer':
        product_number = quality * 1.10
    if product_type == 'sweets':
        product_number = quality * 1.35
    if product_type == 'peanuts':
        product_number = quality * 1.55

print(product_number)
