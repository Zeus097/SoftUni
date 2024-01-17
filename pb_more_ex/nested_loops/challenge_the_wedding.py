men_clients = int(input())
women_clients = int(input())
total_tables = int(input())

for men in range(1, men_clients + 1):
    for women in range(1, women_clients + 1):
        if total_tables <= 0:
            break

        print(f"({men} <-> {women})", end=" ")

        total_tables -= 1
