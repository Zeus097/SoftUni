from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int, gender: str = "Female"):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Meow"
    