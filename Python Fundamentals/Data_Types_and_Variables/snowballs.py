number_of_snowballs = int(input())
best_weight = 0
best_time = 0
best_quality = 0
best_value = 0
for snowballs in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = int((weight / time_needed) ** quality)
    if snowball_value > best_value:
        best_value = snowball_value
        best_weight = weight
        best_time = time_needed
        best_quality = quality

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
