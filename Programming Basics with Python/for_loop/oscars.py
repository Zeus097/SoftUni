actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

total_points = academy_points

for number in range(number_of_jury):
    name_of_jury = input()
    points_from_jury = float(input())
    sum = len(name_of_jury) * points_from_jury / 2
    total_points += sum
    if total_points > 1250.50:
        break

difference = 1250.50 - total_points

if total_points > 1250.50:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
elif total_points <= 1250.50:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")