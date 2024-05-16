from collections import deque


def main():
    green_light_duration = int(input())
    free_window_duration = int(input())

    car_queue = deque()
    total_cars_passed = 0

    while True:
        command = input()

        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break

        if command == "green":
            current_green_light = green_light_duration
            current_free_window = free_window_duration

            while car_queue and current_green_light > 0:
                car = car_queue.popleft()
                car_length = len(car)

                if car_length <= current_green_light:
                    current_green_light -= car_length
                    total_cars_passed += 1
                else:
                    crashed_car = car[current_green_light:]
                    current_free_window -= len(crashed_car)
                    current_green_light = 0

                    if current_free_window >= 0:
                        total_cars_passed += 1
                    else:
                        print("A crash happened!")
                        print(f"{car} was hit at {car[current_free_window]}.")
                        return

        else:
            car_queue.append(command)


if __name__ == "__main__":
    main()
