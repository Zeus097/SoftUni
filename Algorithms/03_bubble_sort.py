def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    
    return nums


nums = [int(x) for x in input().split()]
print(*bubble_sort(nums), sep=' ')


# Input:
# 5 4 3 2 1

# Output:
# 1 2 3 4 5
