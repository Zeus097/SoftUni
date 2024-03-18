import re

dates = input()
pattern = r'\b(\d{2})([-.\/])([A-z][a-z]{2})\2(\d{4})\b'
matches = re.findall(pattern, dates)
for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
