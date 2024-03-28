import re


number_of_sequences = int(input())
for index in range(number_of_sequences):
    barcode = input()
    pattern = r'[@][#]{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])[@][#]{1,}'
    matches = re.findall(pattern, barcode)

    product_group = ''
    for current_number in matches:
        for digit in current_number:
            if digit.isnumeric():
                product_group += digit

    if len(product_group) == 0:
        product_group = '00'

    if len(matches) == 0:
        print("Invalid barcode")
    else:
        print(f"Product group: {product_group}")
