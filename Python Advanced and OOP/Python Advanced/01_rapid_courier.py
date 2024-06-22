from collections import deque


packages_weight = list(map(int, input().split()))
total_packages = len(packages_weight)
couriers_capacities = deque(map(int, input().split()))
total_delivery_weight = 0

while packages_weight and couriers_capacities:
    current_package = packages_weight[-1]
    current_courier = couriers_capacities[0]

    if current_courier > current_package:
        couriers_capacities[0] -= current_package * 2
        if couriers_capacities[0] > 0:
            couriers_capacities.rotate(-1)
        elif couriers_capacities[0] <= 0:
            couriers_capacities.popleft()

        total_delivery_weight += current_package
        packages_weight.pop()
        total_packages -= 1

    elif current_courier < current_package:
        packages_weight[-1] -= current_courier
        total_delivery_weight += current_courier
        couriers_capacities.popleft()

    else:
        total_delivery_weight += packages_weight[-1]
        couriers_capacities.popleft()
        packages_weight.pop()
        total_packages -= 1

print(f"Total weight: {total_delivery_weight} kg")

if total_packages == 0 and len(couriers_capacities) == 0:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages_weight and len(couriers_capacities) == 0:
    print(f"Unfortunately, there are no more available couriers to deliver"
          f" the following packages: {', '.join(map(str, packages_weight))}")

elif couriers_capacities and len(packages_weight) == 0:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers_capacities))} "
          f"but there are no more packages to deliver.")
