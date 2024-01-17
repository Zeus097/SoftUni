num = int(input())

convert_num = str(num)
sorted_num = "".join(sorted(convert_num, reverse=True))

print(int(sorted_num))