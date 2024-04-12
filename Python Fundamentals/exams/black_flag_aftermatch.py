def looting(days_number, daily_loot, expected_loot):
    collected_treasure = 0
    for day in range(1, days_number + 1):
        collected_treasure += daily_loot
        if day % 3 == 0:
            collected_treasure += daily_loot * 0.5

        if day % 5 == 0:
            collected_treasure -= collected_treasure * 0.3

    if collected_treasure >= expected_loot:
        return f"Ahoy! {collected_treasure:.2f} plunder gained."
    else:
        needed_loot_percentage = (collected_treasure / expected_loot) * 100
        return f"Collected only {needed_loot_percentage:.2f}% of the plunder."


days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
looted_treasure = looting(days, daily_plunder, expected_plunder)
print(looted_treasure)
