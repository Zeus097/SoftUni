products_and_quantities = input().split()
search_products = input().split()
products = {}

for index in range(0, len(products_and_quantities), 2):
    product = products_and_quantities[index]
    quantity = int(products_and_quantities[index + 1])
    products[product] = quantity

for product in search_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

