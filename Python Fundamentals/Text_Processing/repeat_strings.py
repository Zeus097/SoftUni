sequence_of_strings = input().split()
concatenated_string = [string * len(string) for string in sequence_of_strings]
print("".join(concatenated_string))
