import re

names = input()
pattern = r'\b[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+\b'
matches = re.findall(pattern, names)
print(" ".join(matches))
