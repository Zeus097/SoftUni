number_of_pages = float(input())
pages_per_hour = float(input())
number_of_days = float(input())

needed_time_for_reading = number_of_pages / pages_per_hour
needed_time_for_one_day = needed_time_for_reading // number_of_days

print(int(needed_time_for_one_day))
