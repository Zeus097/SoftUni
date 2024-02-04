def perfect_number(num):
    proper_divisors = 0
    for current_number in range(1, num):
        if num % current_number == 0:
            proper_divisors += current_number
    if num == proper_divisors:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
perfect_number(number)
