def calc_fibonacci(number):
    num_1 = 1
    num_2 = 1
    result = 0
    for _ in range(number - 1):
        result = num_1 + num_2
        num_1, num_2 = num_2, result
    
    return result


n = int(input())
print(calc_fibonacci(n))


# Input: 5
#Output:  8

# Input: 10
#Output:  89

# Input: 21
#Output:  17711
