from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers) -> None:
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= self.fuel_consumption * kilometers
