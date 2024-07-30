from project.vehicle import Vehicle


from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 500)

    def testing_initialization(self):
        self.assertIsInstance(self.vehicle, Vehicle)
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.horse_power, 500)
        self.assertEqual(self.vehicle.capacity, 100)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def testing_parameters_type(self):
        self.assertTrue(self.vehicle.fuel, float)
        self.assertTrue(self.vehicle.horse_power, float)
        self.assertTrue(self.vehicle.capacity, float)
        self.assertTrue(self.vehicle.fuel_consumption, float)

    def testing_drive_method_case_when_needed_fuel_is_more_than_fuel(self):
        self.vehicle.fuel = 50
        kilometers = 80
        needed_fuel = kilometers * self.vehicle.fuel_consumption
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(needed_fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def testing_drive_method_case_when_needed_fuel_is_less_than_fuel(self):
        self.vehicle.fuel = 150
        kilometers = 80
        needed_fuel = kilometers * self.vehicle.fuel_consumption

        self.vehicle.drive(needed_fuel)

        self.assertEqual(self.vehicle.fuel, 25)

    def testing_refill_method_when_fuel_capacity_is_exceeded(self):
        fuel = 100
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def testing_refill_method_when_fuel_capacity_is_not_exceeded(self):
        self.vehicle.fuel = 50
        fuel = 20
        self.vehicle.refuel(fuel)
        self.assertEqual(self.vehicle.fuel, 70)

    def testing_string_method(self):
        self.assertEqual(f"The vehicle has 500 horse power "
                         f"with 100 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == '__main__':
    main()
