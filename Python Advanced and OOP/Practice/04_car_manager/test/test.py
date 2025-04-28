from project.car import Car

# For Judge...
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(
            'VW',
            'Passat',
            8,
            60
        )

    def test_init(self):
        self.assertIsInstance(self.car, Car)
        self.assertEqual(self.car.make, 'VW')
        self.assertEqual(self.car.model, 'Passat')
        self.assertEqual(self.car.fuel_consumption, 8)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_returning_case(self):
        result = self.car.make
        self.assertEqual(result, 'VW')

    def test_make_with_valid_value(self):
        self.car.make = 'Audi'
        self.assertEqual(self.car.make, 'Audi')

    def test_make_with_empty_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_model_with_valid_value(self):
        self.car.model = 'A5'
        self.assertEqual(self.car.model, 'A5')

    def test_model_with_empty_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_fuel_with_valid_value(self):
        self.car.fuel_consumption = 8
        self.assertEqual(self.car.fuel_consumption, 8)

    def test_fuel_consumption_with_negative_or_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -8
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_fuel_capacity_with_valid_value(self):
        self.car.fuel_capacity = 60
        self.assertEqual(self.car.fuel_capacity, 60)

    def test_fuel_capacity_with_negative_or_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -60
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount_with_valid_value(self):
        self.car.fuel_amount = 0
        self.assertEqual(self.car.fuel_amount, 0)

    def test_fuel_amount_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -8
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel_fuel_amount_greater_than_fuel_capacity_case(self):
        self.car.fuel_amount = 50
        self.car.refuel(20)

        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_with_negative_value_case(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))
        self.assertEqual(self.car.fuel_amount, 0)

    def test_drive_with_enough_fuel_case(self):
        self.car.fuel_amount = 60
        needed_fuel = 5
        self.car.drive(needed_fuel)
        self.assertEqual(self.car.fuel_amount, 59.6)

    def test_drive_without_enough_fuel_case(self):
        self.car.fuel_amount = 1
        needed_fuel = 50
        with self.assertRaises(Exception) as ex:
            self.car.drive(needed_fuel)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(self.car.fuel_amount, 1)


if __name__ == '__main__':
    main()
