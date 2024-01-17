first_number_top = int(input())
second_number_top = int(input())
third_number_top = int(input())

for num_1 in range(1, first_number_top + 1):
    if num_1 % 2 == 0:
        for num_2 in range(1, second_number_top + 1):
            if num_2 > 1:
                for i in range(2, num_2):
                    if num_2 % i == 0:
                        break
                else:
                    for num_3 in range(1, third_number_top + 1):
                        if num_3 % 2 == 0:
                            print(num_1,num_2,num_3)
