def average_value(number_sequence):
    return sum(number_sequence) // len(number_sequence)


def sequence_calculation(number_sequence, current_average_value):
    number_sequence.sort(reverse=True)
    counter = 0
    needed_numbers = []
    for index in range(len(number_sequence)):
        if number_sequence[index] > current_average_value:
            needed_numbers.append(number_sequence[index])
            counter += 1
            if counter == 5:
                break
    return ' '.join(map(str, needed_numbers))


integers = list(map(int, input().split()))
average_sum = average_value(integers)
top_numbers = sequence_calculation(integers, average_sum)

if len(top_numbers) > 0:
    print(top_numbers)
else:
    print("No")
