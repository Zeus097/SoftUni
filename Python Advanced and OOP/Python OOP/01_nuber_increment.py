def number_increment(numbers):

    def increase():

        return [num + 1 for num in numbers]

    return increase()


# Test code

print(number_increment([1, 2, 3]))
