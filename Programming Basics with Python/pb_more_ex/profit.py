coins_1lv = int(input())
coins_2lv = int(input())
coins_5lv = int(input())
amount = int(input())

for count_1lv in range(coins_1lv + 1):
    for count_2lv in range(coins_2lv + 1):
        for count_5lv in range(coins_5lv + 1):
            total_amount = count_1lv + 2 * count_2lv + 5 * count_5lv
            if total_amount == amount:
                print(f"{count_1lv} * 1 lv. + {count_2lv} * 2 lv. + {count_5lv} * 5 lv. = {amount} lv.")
