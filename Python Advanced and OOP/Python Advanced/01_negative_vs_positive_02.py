def nums_operation(nums):
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)
    return positive_sum, negative_sum


numbers = list(map(int, input().split()))
positive, negative = nums_operation(numbers)

print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
