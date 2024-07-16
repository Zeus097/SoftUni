from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int, gender: str = "Male"):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Hiss"
