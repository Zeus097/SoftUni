rest_days = int(input())

max_minutes = 30000
total_days_year = 365
total_rest_days_per_year = 20
total_working_days = total_days_year - rest_days

work_day_game_time_in_minutes = 63
free_day_game_time_in_minutes = 127

rest_days_game_time = rest_days * free_day_game_time_in_minutes
work_days_game_time = total_working_days * work_day_game_time_in_minutes
total_game_minutes = rest_days_game_time + work_days_game_time
diff = abs(max_minutes - total_game_minutes)
hours = diff // 60
minutes = diff % 60

if max_minutes <= total_game_minutes:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:

    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")