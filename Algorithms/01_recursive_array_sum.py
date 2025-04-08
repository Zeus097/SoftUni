# NOTE: In practice, this recursion should not be used here (instead use an iterative solution).


def arrau_sum(nums, index):
    if index >= len(nums) - 1:
        return nums[index]
    
    return nums[index] + arrau_sum(nums, index + 1)


nums = list(map(int, input().split()))
print(arrau_sum(nums, 0))


# Input: 1 2 3 4
# Output: 10

# Input: -1 0 1
# Output: 0
