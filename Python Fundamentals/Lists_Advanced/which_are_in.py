first_string = input().split(", ")
second_string = input().split(", ")
new_string = []
for first in first_string:
    for second in second_string:
        if first in second:
            new_string.append(first)
            break
print(new_string)
