city = input()
sales = float(input())
sales_number = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        sales_number = sales * 0.05
        print(f'{sales_number:.2f}')
    elif 500 < sales <= 1000:
        sales_number = sales * 0.07
        print(f'{sales_number:.2f}')
    elif 1000 < sales <= 10000:
        sales_number = sales * 0.08
        print(f'{sales_number:.2f}')
    elif sales > 10000:
        sales_number = sales * 0.12
        print(f'{sales_number:.2f}')
    else:
        print('error')

elif city == 'Varna':
    if 0 <= sales <= 500:
        sales_number = sales * 0.045
        print(f'{sales_number:.2f}')
    elif 500 < sales <= 1000:
        sales_number = sales * 0.075
        print(f'{sales_number:.2f}')
    elif 1000 < sales <= 10000:
        sales_number = sales * 0.1
        print(f'{sales_number:.2f}')
    elif sales > 10000:
        sales_number = sales * 0.13
        print(f'{sales_number:.2f}')
    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        sales_number = sales * 0.055
        print(f'{sales_number:.2f}')
    elif 500 < sales <= 1000:
        sales_number = sales * 0.08
        print(f'{sales_number:.2f}')
    elif 1000 < sales <= 10000:
        sales_number = sales * 0.12
        print(f'{sales_number:.2f}')
    elif sales > 10000:
        sales_number = sales * 0.145
        print(f'{sales_number:.2f}')
    else:
        print('error')

else:
    print('error')