from math import ceil

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

remaining_time = break_duration - lunch_time - rest_time
needed_time = abs(episode_duration - remaining_time)
difference = ceil(needed_time)

if remaining_time >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {difference} more minutes.")
