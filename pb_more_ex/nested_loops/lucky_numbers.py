number = int(input())
flag = False

for num_1 in range(1, number):
    if num_1 > 9:
        break
    for num_2 in range(1, number):
        if num_2 > 9:
            break
        for num_3 in range(1, number):
            if num_3 > 9:
                break
            for num_4 in range(1, number):
                if num_4 > 9:
                    break
                first_sum = num_1 + num_2
                last_sum = num_3 + num_4
                total_sum = num_1 + num_2 + num_3 + num_4
                if first_sum == last_sum:
                    if number % first_sum == 0:
                        print(f"{num_1}{num_2}{num_3}{num_4}",end=" ")
