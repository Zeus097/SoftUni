from collections import deque


fuel = list(map(int, input().split()))
consumption_index = deque(map(int, input().split()))
needed_fuel = deque(map(int, input().split()))
altitude_count = 0
seek_altitude = 1
altiude_reached = []

while True:
    if fuel[-1] - consumption_index[0] >= needed_fuel[0]:
        fuel.pop()
        consumption_index.popleft()
        needed_fuel.popleft()
        altitude_count += 1
        altiude_reached.append(f"Altitude {altitude_count}")
        print(f"John has reached: Altitude {seek_altitude}")
        if len(fuel) == 0 or len(consumption_index) == 0 or len(needed_fuel) == 0:
            print("John has reached all the altitudes and managed to reach the top!")
            break

    elif fuel[-1] - consumption_index[0] < needed_fuel[0]:
        print(f"John did not reach: Altitude {seek_altitude}")
        if len(altiude_reached) > 0:
            print("John failed to reach the top.")
            print("Reached altitudes: ", end="")
            print(*altiude_reached, sep=', ')
        else:
            print("John failed to reach the top.")
            print("John didn't reach any altitude.")
        break

    seek_altitude += 1
