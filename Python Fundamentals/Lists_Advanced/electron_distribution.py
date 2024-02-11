def electrons_in_shell(number_of_electrons):
    filled_shells = []

    for shell in range(1, number_of_electrons + 1):

        electron_distribution = 2 * shell ** 2

        if electron_distribution > number_of_electrons:
            filled_shells.append(number_of_electrons)
            number_of_electrons -= electron_distribution
            break
        else:
            filled_shells.append(electron_distribution)
            number_of_electrons -= electron_distribution

        if number_of_electrons <= 0:
            break

    return filled_shells


electrons = int(input())
shell = electrons_in_shell(electrons)

print(shell)
