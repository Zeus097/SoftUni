import unittest
from app import calculate_bmi, calculate_calories_burned


class TestCalculateBMI(unittest.TestCase):
    def test_bmi_with_high_weight_and_height(self):
        message = "The calculated BMI is not correct"
        self.assertAlmostEqual(calculate_bmi(95, 1.81), 28.997893837184456, msg=message)

    def test_bmi_with_low_weight_and_height(self):
        message = "The calculated BMI is not correct"
        self.assertAlmostEqual(calculate_bmi(50, 1.00), 50, msg=message)


class TestCalculateCaloriesBurned(unittest.TestCase):
    def test_low_calories_burned(self):
        message = "The calculated calories burned are not correct"
        self.assertAlmostEqual(calculate_calories_burned(20), 133.4, msg=message)

    def test_high_calories_burned(self):
        message = "The calculated calories burned are not correct"
        self.assertAlmostEqual(calculate_calories_burned(100), 667, msg=message)


if __name__ == '__main__':
    unittest.main()