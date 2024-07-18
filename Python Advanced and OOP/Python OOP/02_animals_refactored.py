from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Chiken(Animal):
    def make_sound(self):
        return "co-co-co"


# Testing

def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(f"{animal.name.upper()} sound : {animal.make_sound()}")


animal_collection = [Cat('cat'), Dog('dog'), Chiken('chicken')]
animal_sound(animal_collection)
