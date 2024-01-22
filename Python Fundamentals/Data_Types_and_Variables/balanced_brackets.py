number_of_lines = int(input())
opened_brakes = False
closed_brakes = False
opened_brakes_counter = 0
closed_brakes_counter = 0

for brakes in range(number_of_lines):
    current_string = input()

    if brakes + 1 == number_of_lines:
        break

    if current_string == "(":
        if opened_brakes_counter > closed_brakes_counter:
            closed_brakes = False
            break
        opened_brakes_counter += 1
        opened_brakes = True
    if current_string == ")" and opened_brakes:
        closed_brakes_counter += 1
        closed_brakes = True

if opened_brakes and closed_brakes:
    print("BALANCED")
else:
    print("UNBALANCED")
