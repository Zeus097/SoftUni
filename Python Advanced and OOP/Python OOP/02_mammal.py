class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type_, sound):
        self.name = name
        self.type = type_
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    @staticmethod
    def get_kingdom():
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


# Test code

# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())
