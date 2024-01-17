# Oscars // For Loop,Ex - 6

actor_name = input()
academy_points = float(input())
jury_number = int(input())
points_given = 0
total_points = 0

for points in range(jury_number):
    jury_name = input()
    jury_points = float(input())
    points_given +=(len(jury_name) * jury_points / 2)
    total_points = points_given + academy_points
    if total_points > 1250.5:
        break
difference = abs(1250.5 - total_points)
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")