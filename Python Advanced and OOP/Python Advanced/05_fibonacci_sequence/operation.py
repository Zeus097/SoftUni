from logic import creating_sequence


located_numbers = []
while True:
    input_text = input().split()
    numbers = [0, 1]

    if input_text == "Stop":
        break

    elif input_text[0] == "Create":
        count = int(input_text[-1])
        located_numbers.extend(creating_sequence(count, numbers))
        print(*located_numbers, sep=" ")
    elif input_text[0] == "Locate":
        number = int(input_text[-1])
        if number in located_numbers:
            num_index = located_numbers.index(number)
            located_numbers.clear()
            print(f"The number - {number} is at index {num_index}")
        else:
            print(f"The number {number} is not in the sequence")
