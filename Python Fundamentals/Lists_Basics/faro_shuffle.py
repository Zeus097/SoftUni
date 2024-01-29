deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    middle_half_of_the_deck = len(deck_of_cards) // 2
    left_side_of_the_deck = deck_of_cards[:middle_half_of_the_deck]
    right_side_of_the_deck = deck_of_cards[middle_half_of_the_deck:]

    deck_after_shuffle = []

    for card_index in range(len(right_side_of_the_deck)):
        deck_after_shuffle.append(left_side_of_the_deck[card_index])
        deck_after_shuffle.append(right_side_of_the_deck[card_index])

    deck_of_cards = deck_after_shuffle

print(deck_of_cards)
