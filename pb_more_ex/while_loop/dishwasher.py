detergent = int(input())
detergent_in_ml = detergent * 750
counter = 0
cleaned_plates = 0
cleaned_pots = 0
no_more_detergent = False
needed_detergent = 0
command = input()

while command != "End":
    number_of_dishes = int(command)
    counter += 1
    if counter != 3:
        if detergent_in_ml >= number_of_dishes * 5:
            detergent_in_ml -= number_of_dishes * 5
            cleaned_plates += number_of_dishes
        else:
            needed_detergent = number_of_dishes * 5 - detergent_in_ml
            no_more_detergent = True
            break
    else:
        counter = 0
        if detergent_in_ml >= number_of_dishes * 15:
            detergent_in_ml -= number_of_dishes * 15
            cleaned_pots += number_of_dishes
        else:
            needed_detergent = number_of_dishes * 15 - detergent_in_ml
            no_more_detergent = True
            break
    command = input()

if command == "End":
    print("Detergent was enough!")
    print(f"{cleaned_plates} dishes and {cleaned_pots} pots were washed.")
    print(f"Leftover detergent {detergent_in_ml} ml.")

if no_more_detergent:
    print(f"Not enough detergent, {needed_detergent} ml. more necessary!")