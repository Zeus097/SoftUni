from project.car import Car


from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('VW', 'Passat B6', 10, 100)

    def test_init_case(self):
        self.assertIsInstance(self.car, Car)
        self.assertEqual(self.car.make, 'VW')
        self.assertEqual(self.car.model, 'Passat B6')
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 100)

    def testing_car_change_make_validation_with_valid_name(self):
        self.car.make = 'Audi'
        self.assertEqual(self.car.make, 'Audi')

    def testing_car_change_name_validation_with_empty_invalid_name(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def testing_car_change_model_validation_with_valid_name(self):
        self.car.model = 'Golf 3'
        self.assertEqual(self.car.model, 'Golf 3')

    def testing_car_change_model_validation_with_empty_invalid_name(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def testing_fuel_consumption_validation_with_positive_value(self):
        self.car.fuel_consumption = 10
        self.assertEqual(self.car.fuel_consumption, 10)

    def testing_fuel_consumption_validation_with_value_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def testing_fuel_consumption_validation_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -10
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def testing_fuel_capacity_validation_with_positive_value(self):
        self.car.fuel_capacity = 10
        self.assertEqual(self.car.fuel_capacity, 10)

    def testing_fuel_capacity_validation_with_value_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def testing_fuel_capacity_validation_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -10
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def testing_fuel_amount_validation_with_positive_fuel_amount(self):
        self.car.fuel_amount = 10
        self.assertEqual(self.car.fuel_amount, 10)

    def testing_fuel_amount_validation_with_zero_amount(self):
        self.car.fuel_amount = 0
        self.assertEqual(self.car.fuel_amount, 0)

    def testing_fuel_amount_validation_with_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def testing_refill_with_positive_fuel_amount_less_than_the_fuel_capacity(self):
        self.car.fuel_amount = 10
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 60)

    def testing_refill_with_positive_fuel_amount_greater_than_the_fuel_capacity(self):
        self.car.fuel_amount = 10
        self.car.refuel(500)
        self.assertEqual(self.car.fuel_amount, 100)

    def testing_refill_with_zero_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = 10
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def testing_refill_with_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = 10
            self.car.refuel(-500)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_driving_method_with_enough_fuel_amount(self):
        self.car.fuel_amount = 100
        self.car.fuel_consumption = 10
        needed_fuel = 97
        self.car.drive(30)
        self.assertEqual(int(self.car.fuel_amount), needed_fuel)

    def test_driving_method_without_enough_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(150)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    main()
