number_of_guests = int(input())
reservation = set()

for _ in range(number_of_guests):
    reservation_code = input()
    reservation.add(reservation_code)


while True:
    guest = input()
    if guest == 'END':
        break
    reservation.remove(guest)

print(len(reservation))
for num in sorted(reservation):
    print(num)
