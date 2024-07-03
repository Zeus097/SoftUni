from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers) -> None:
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= self.fuel_consumption * kilometers
