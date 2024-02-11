def groups_of_numbers(numbers, group_name):
    while numbers:
        group = []
        group_name += 10

        list_of_numbers = [group.append(digit) for digit in numbers if digit <= group_name]
        subtract_grouped_numbers = [numbers.remove(digit) for digit in group if digit in numbers]

        print(f"Group of {group_name}'s: {group}")


number = list(map(int, input().split(", ")))
group_name = 0

groups_of_numbers(number, group_name)
