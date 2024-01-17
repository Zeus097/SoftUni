start_interval = int(input())
end_interval = int(input())

for num_1 in range(start_interval, end_interval + 1):
    for num_2 in range(start_interval, end_interval + 1):
        for num_3 in range(start_interval, end_interval + 1):
            for num_4 in range(start_interval, end_interval + 1):
                if num_1 > num_4:
                    if (num_2 + num_3) % 2 == 0:
                        if (num_1 % 2 == 0 and num_4 % 2 != 0) or (num_1 % 2 != 0 and num_4 % 2 == 0):
                            print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")
