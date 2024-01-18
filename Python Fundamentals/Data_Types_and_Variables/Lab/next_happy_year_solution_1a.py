year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    if len(set(year_as_string)) == len(year_as_string):
        break

print(year)
