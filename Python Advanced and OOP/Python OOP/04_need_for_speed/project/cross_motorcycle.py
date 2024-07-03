from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers) -> None:
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption
