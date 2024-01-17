day_of_the_week = input()
data = 0

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday':
    data = 12
elif day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday':
    data = 14
elif day_of_the_week == 'Friday':
    data = 12
elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    data = 16

print(data)
