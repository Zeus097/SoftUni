from typing import Optional


class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people) -> Optional[str]:
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people
        self.capacity -= people

    def free_room(self) -> Optional[str]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.capacity += self.guests
        self.guests = 0
