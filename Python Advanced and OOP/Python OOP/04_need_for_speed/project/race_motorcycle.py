from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers) -> None:
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= self.fuel_consumption * kilometers
