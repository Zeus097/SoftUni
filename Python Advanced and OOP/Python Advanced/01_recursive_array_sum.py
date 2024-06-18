def calc_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calc_sum(nums, idx + 1)


numbers = list(map(int, input().split()))
result = calc_sum(numbers)
print(result)
