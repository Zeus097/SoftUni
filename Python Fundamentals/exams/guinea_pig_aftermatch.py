def pig_care(food, hay, cover, weight):
    counter = 0

    while counter < 30:
        if food <= 0 or hay <= 0 or cover <= 0:
            break

        counter += 1
        food -= 300
        if counter % 2 == 0:
            hay -= food * 0.05

        if counter % 3 == 0:
            cover -= weight // 3

    return food, hay, cover, weight


def remaining_food_convert(food, hay, cover):
    food /= 1000
    hay /= 1000
    cover /= 1000
    return food, hay, cover


def main_program():
    food_quantity_in_kg = float(input())
    hay_quantity_in_kg = float(input())
    cover_quantity_in_kg = float(input())
    pig_weight_in_kg = float(input())

    food_quantity_in_gr = food_quantity_in_kg * 1000
    hay_quantity_in_gr = hay_quantity_in_kg * 1000
    cover_quantity_in_gr = cover_quantity_in_kg * 1000
    pig_weight_in_gr = pig_weight_in_kg * 1000

    food_left_in_gr, hay_left_in_gr, cover_left_in_gr, pig_weight = pig_care(food_quantity_in_gr, hay_quantity_in_gr,
                                                                             cover_quantity_in_gr,
                                                                             pig_weight_in_gr)

    food_left_in_kg, hey_left_in_kg, cover_left_in_kg = remaining_food_convert(food_left_in_gr,
                                                                               hay_left_in_gr,
                                                                               cover_left_in_gr)

    if food_left_in_kg > 0 and hey_left_in_kg > 0 and cover_left_in_kg > 0:
        print(f"Everything is fine! Puppy is happy! Food: {food_left_in_kg:.2f}, "
              f"Hay: {hey_left_in_kg:.2f}, "
              f"Cover: {cover_left_in_kg:.2f}.")
    else:
        print("Merry must go to the pet store!")


if __name__ == '__main__':
    main_program()
