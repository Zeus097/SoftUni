number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    reservation_code = input()

    if len(reservation_code) != 8:
        continue

    guests.add(reservation_code)

command = input()
while command != 'END':
    guests.remove(command)

    command = input()


print(len(guests))

sorted_guests = sorted(guests)
print(*sorted_guests, sep='\n')
