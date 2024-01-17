from math import inf

number = int(input())

even_sum = 0
even_min = inf
even_max = - inf

odd_sum = 0
odd_min = inf
odd_max = - inf


for num in range(1, number +1):
    current_number = float(input())
    if num % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

print(f"OddSum={odd_sum:.02f},")
if odd_min == inf:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.02f},")
if odd_max == - inf:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.02f},")
print(f"EvenSum={even_sum:.02f},")
if even_min == inf:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.02f},")
if even_max == - inf:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.02f}")


