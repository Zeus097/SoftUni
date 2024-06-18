def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


numbers = list(map(int, input().split()))
sort_nuims = insertion_sort(numbers)
print(*sort_nuims)
