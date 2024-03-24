import re


text = input()
pattern = r'(?i)([|#])([a-z\s]+)\1(\d{2}/\d{2}\/\d{2})\1(\d+)\1'
match_info = re.findall(pattern, text)
total_calories = sum([int(match[3]) for match in match_info])
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for item in match_info:
    item_name = item[1]
    expiration_date = item[2]
    calories = item[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
