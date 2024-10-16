class vowels:
    def __init__(self, text: str):
        self.text= text
        vowels_const = ['a', 'i', 'e', 'u', 'y', 'o']
        self.found_vowels = [char for char in self.text if char.lower() in vowels_const]
        self.current_index = 0
        self.end_index = len(self.found_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration
        index = self.current_index
        self.current_index += 1
        return self.found_vowels[index]


# Test Code

# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


# Output

# A
# e
# i
# u
# y
# o
