hour = int(input())
minute = int(input())
minute += 15
hour += minute // 60
minute %= 60

if hour > 23:
    hour = 0

if minute < 10:
    print(f'{hour}:0{minute}')
else:
    print(f'{hour}:{minute}')



