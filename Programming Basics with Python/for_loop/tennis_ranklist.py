from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
current_points = 0
sum_points = 0
won_tournaments = 0

for tournaments in range(number_of_tournaments):
    type_of_tournament = input()
    if type_of_tournament == "W":
        current_points += 2000
        won_tournaments += 1
    elif type_of_tournament == "F":
        current_points += 1200
    elif type_of_tournament == "SF":
        current_points += 720
    average_points = floor(current_points / number_of_tournaments)
    final_points = current_points + starting_points
    percentage_won_tournaments = (won_tournaments / number_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percentage_won_tournaments:.2f}%")