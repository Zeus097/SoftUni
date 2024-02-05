def tribonacci_sequence(number):
    sequence = [1, 1, 2]

    for index in range(3, number):
        next_number = sequence[index - 1] + sequence[index - 2] + sequence[index - 3]
        sequence.append(next_number)

    print(" ".join(map(str, sequence[:number])))

number = int(input())
tribonacci_sequence(number)
