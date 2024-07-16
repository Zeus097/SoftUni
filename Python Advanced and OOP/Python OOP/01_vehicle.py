from abc import ABC, abstractmethod


class Vehicle(ABC):
    CAR_AIR_CONDITIONER_CONSUMPTION = 0.9
    TRUCK_AIR_CONDITIONER_CONSUMPTION = 1.6
    TRUCK_FUEL_COEFFICIENT = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + Vehicle.CAR_AIR_CONDITIONER_CONSUMPTION) * distance
        self.fuel_quantity -= needed_fuel if needed_fuel <= self.fuel_quantity else 0
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    pass

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + Vehicle.TRUCK_AIR_CONDITIONER_CONSUMPTION) * distance
        self.fuel_quantity -= needed_fuel if needed_fuel <= self.fuel_quantity else 0
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Vehicle.TRUCK_FUEL_COEFFICIENT


# Test code
# Part I

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

# Part II

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
