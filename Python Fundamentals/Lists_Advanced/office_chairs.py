def calculating_places(number_of_rooms):
        total_chairs = 0

        for room_number in range(1, number_of_rooms + 1):
                places = input().split()
                chairs = places[0]
                visitors = int(places[1])
                total_chairs += len(chairs)

                if len(chairs) < visitors:
                        needed_chairs = visitors - len(chairs)
                        print(f"{needed_chairs} more chairs needed in room {room_number}")
                total_chairs -= visitors

        return total_chairs



number_of_rooms = int(input())
total_chairs = calculating_places(number_of_rooms)

if total_chairs >= 0:
        print(f"Game On, {total_chairs} free chairs left")
