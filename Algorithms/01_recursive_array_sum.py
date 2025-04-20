def calc_recursive_array_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calc_recursive_array_sum(nums, idx + 1)


array = [int(x) for x in input().split()]
print(calc_recursive_array_sum(array))
