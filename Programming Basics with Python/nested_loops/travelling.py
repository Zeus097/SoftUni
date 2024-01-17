destination = input()
needed_sum = 0

while destination != "End":
    minimal_budget = float(input())
    while minimal_budget > needed_sum:
        savings = float(input())
        needed_sum += savings

    print(f"Going to {destination}!")

    destination = input()
    needed_sum = 0