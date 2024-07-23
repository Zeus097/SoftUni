from math import sqrt


def get_primes(nums):
    for num in nums:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num


# # Test code // Output:[2, 3, 5]
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


# # Test code // Output:[]
#
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))
