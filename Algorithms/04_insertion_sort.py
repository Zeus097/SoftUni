def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1

    return nums

nums = [int(x) for x in input().split()]
print(*insertion_sort(nums), sep=' ')


# Input:
# 5 4 3 2 1

# Output:
# 1 2 3 4 5
