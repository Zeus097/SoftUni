some_string = input().split()
even_string = [index for index in some_string if int(len(index) % 2 == 0)]
print("\n".join(even_string))
