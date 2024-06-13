def creating_sequence(n, nums):

    for _ in range(n - 2):
        fibonacci_num = nums[-1] + nums[-2]
        nums.append(fibonacci_num)
    return nums
