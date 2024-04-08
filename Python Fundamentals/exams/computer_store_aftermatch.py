def calculate_taxes(raw_price):
    return raw_price * 0.2


def printing_output(raw_price, tax_money, total_sum):
    return (f"Congratulations you've just bought a new computer!\n"
            f"Price without taxes: {raw_price:.2f}$\n"
            f"Taxes: {tax_money:.2f}$\n"
            f"-----------\n"
            f"Total price: {total_sum:.2f}$")


def main():
    price_without_taxes = 0
    total_price = 0
    while True:
        command = input()
        if command == 'special' or command == 'regular':
            taxes = calculate_taxes(price_without_taxes)
            total_price += price_without_taxes + taxes
            if price_without_taxes == 0:
                print('Invalid order!')
                break
            elif command == 'special':
                total_price *= 0.9
            result = printing_output(price_without_taxes, taxes, total_price)
            print(result)
            break

        current_price = float(command)
        if current_price < 0:
            print('Invalid price!')
            continue

        price_without_taxes += current_price


if __name__ == '__main__':
    main()
