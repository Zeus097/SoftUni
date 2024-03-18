import re

string = input()
while string:
    pattern = r'\d+'
    result = re.findall(pattern, string)
    if result:
        print(' '.join(result), end=' ')
    string = input()
