from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> None:
        room = next((room for room in self.rooms if room.number == room_number), None)
        if room:
            room.take_room(people)

    def free_room(self, room_number) -> None:
        room = next((room for room in self.rooms if room.number == room_number), None)
        if room:
            room.free_room()

    def status(self) -> str:
        return (f"Hotel {self.name} has {sum([room.guests for room in self.rooms])} total guests\n"
                f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n"
                f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}")
