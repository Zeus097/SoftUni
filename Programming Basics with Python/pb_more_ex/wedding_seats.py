last_sector = input()
num_rows_first_sector = int(input())
num_places_odd_row = int(input())
total_seats = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    num_rows_sector = num_rows_first_sector + (sector - ord('A'))

    for row in range(1, num_rows_sector + 1):
        num_places = num_places_odd_row if row % 2 != 0 else num_places_odd_row + 2
        for place in range(num_places):
            print(f"{chr(sector)}{row}{chr(ord('a') + place)}")
            total_seats += 1

print(total_seats)
