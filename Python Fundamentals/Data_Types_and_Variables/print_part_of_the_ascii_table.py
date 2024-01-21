start_line = int(input())
finish_line = int(input())

for symbols in range(start_line, finish_line + 1):
    print(chr(symbols), end=" ")


# slicing solution
#
# start_line = int(input())
# finish_line = int(input())
# last_string = ""
# for symbols in range(start_line, finish_line + 1):
#     last_string += f"{chr(symbols)} "
# print(last_string[:-1])
#
#
# another solution for cutting the space after the last print is with conditional statement
# comparing the last_string with finish_line and if it's last - we print without space.
