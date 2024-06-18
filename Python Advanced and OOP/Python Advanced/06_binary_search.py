def binary_search(numbers, t):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]

        if mid_el == t:
            return mid_idx
        if mid_el < t:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


nums = list(map(int, input().split()))
target = int(input())
print(binary_search(nums, target))
