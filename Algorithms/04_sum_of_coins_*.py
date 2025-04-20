def choose_coins(coins, target_sum):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while target_sum != 0 and index < len(coins):
        count_coins = target_sum // coins[index]

        target_sum %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if target_sum != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"
        for value, count in used_coins.items():
            result += f"{count} coin(s) with value {value}\n"
        return result.strip()


coins_input = list(map(int, input().split(', ')))
target_sum_input = int(input())

print(choose_coins(coins_input, target_sum_input))
