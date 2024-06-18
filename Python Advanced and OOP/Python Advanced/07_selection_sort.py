def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for cur_idx in range(idx + 1, len(nums)):
            if nums[cur_idx] < nums[min_idx]:
                min_idx = cur_idx
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


numbers = list(map(int, input().split()))
selection_sort(numbers)
print(*numbers)
