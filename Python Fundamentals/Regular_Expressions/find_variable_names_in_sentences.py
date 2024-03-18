import re

line = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
result = re.findall(pattern, line)
print(','.join(result))
