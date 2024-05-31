numbers = list(map(int, input().split()))
positive_nums = 0
negative_nums = 0

for number in numbers:
    if number > 0:
        positive_nums += number
    else:
        negative_nums += number

print(negative_nums)
print(positive_nums)
if positive_nums > abs(negative_nums):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
