import unittest
from app import calculate_bmi, filter_underweight_people, filter_normal_weight_people, filter_overweight_people, filter_obesity_people


class TestFilters(unittest.TestCase):
    def test_filter_underweight_people(self):
        example = [{"duration": 20.0, "height": 180.0, "name": "John", "weight": 30.0}]
        expected = [{"duration": 20.0, "height": 180.0, "name": "John", "weight": 30.0}]
        message = "The filtered underweight people list is not correct"
        self.assertEqual(filter_underweight_people(example), expected, msg=message)

    # Add similar tests for other filtering functions...


if __name__ == '__main__':
    unittest.main()
