class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.count + 1 <= len(self.string) -1:
            self.count += 1
            if self.string[self.count].lower() in self.vowels:
                return self.string[self.count]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
