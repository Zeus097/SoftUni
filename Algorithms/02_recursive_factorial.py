# NOTE: In practice, this recursion should not be used here (instead use an iterative solution).


def recursive_factorial(num):
    if num == 0:
        return 1
    
    return num * recursive_factorial(num - 1)


num = int(input())
print(recursive_factorial(num))

# Input: 5
# Output: 120

# Input: 10
# Output: 3628800
