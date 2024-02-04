def smallest_number(num1, num2, num3):
    return min(num1, num2, num3)

first_number = int(input())
second_number = int(input())
third_number = int(input())

the_smallest_number = smallest_number(first_number, second_number, third_number)
print(the_smallest_number)
