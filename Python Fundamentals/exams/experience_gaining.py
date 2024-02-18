needed_experience = float(input())
battles_count = int(input())
total_experience_gained = 0
counter = 0

for current_battle in range(1, battles_count + 1):
    experience_earned = float(input())
    total_experience_gained += experience_earned
    counter += 1
    if current_battle % 15 == 0:
        total_experience_gained += experience_earned * 0.5

    if current_battle % 3 == 0:
        total_experience_gained += experience_earned * 0.15
    if current_battle % 5 == 0:
        total_experience_gained -= experience_earned * 0.1

    if total_experience_gained >= needed_experience:
        break

if total_experience_gained >= needed_experience:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    needed_experience -= total_experience_gained
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
