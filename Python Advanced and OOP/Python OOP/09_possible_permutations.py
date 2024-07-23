from itertools import permutations


def possible_permutations(ls):
    for perm in permutations(ls):
        yield list(perm)


# # Test code
#
# [print(n) for n in possible_permutations([1, 2, 3])]


# # Test code
#
# [print(n) for n in possible_permutations([1])]
