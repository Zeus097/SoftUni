import unittest
from app import main_program


class TestMainProgram(unittest.TestCase):
    def test_people_data(self):
        expected = [{'duration': 60.0, 'height': 2.00, 'name': 'Zeus', 'weight': 90.0}]
        message = "The generated people data is not correct"
        self.assertEqual(main_program(), expected, msg=message)


if __name__ == '__main__':
    unittest.main()
