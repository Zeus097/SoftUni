number_of_pieces = int(input())
collection = {}
for _ in range(number_of_pieces):
    piece_name, composer_name, piece_key = input().split("|")
    collection[piece_name] = {'COMPOSER': composer_name, 'PIECE_KEY': piece_key}

while True:
    command = input()
    if command == 'Stop':
        break

    action = command.split('|')
    if action[0] == 'Add':
        current_piece_name = action[1]
        current_composer_name = action[2]
        current_piece_key = action[3]
        if current_piece_name not in collection:
            collection[current_piece_name] = {'COMPOSER': current_composer_name, 'PIECE_KEY': current_piece_key}
            print(f"{current_piece_name} by {current_composer_name} in {current_piece_key} added to the collection!")
        else:
            print(f"{current_piece_name} is already in the collection!")

    elif action[0] == 'Remove':
        current_piece_name = action[1]
        if current_piece_name in collection:
            del collection[current_piece_name]
            print(f"Successfully removed {current_piece_name}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")

    elif action[0] == 'ChangeKey':
        current_piece_name = action[1]
        current_piece_key = action[2]
        if current_piece_name in collection:
            collection[current_piece_name]['PIECE_KEY'] = current_piece_key
            print(f"Changed the key of {current_piece_name} to {current_piece_key}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")
for piece in collection:
    composer = collection[piece]['COMPOSER']
    key = collection[piece]['PIECE_KEY']
    print(f"{piece} -> Composer: {composer}, Key: {key}")
