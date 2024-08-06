from project.robot import Robot


from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot('id_1', 'Humanoids', 100, 1000)

    def test_initialization(self):
        self.assertIsInstance(self.robot, Robot)
        self.assertEqual('id_1', self.robot.robot_id)
        self.assertEqual('Humanoids', self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_case_with_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'invalid'
        self.assertEqual(str(ve.exception), "Category should be one of "
                                            "'['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_category_case_with_valid_category(self):
        robot = Robot('id_1', 'Humanoids', 100, 1000)
        self.assertEqual(robot.category, 'Humanoids')

    def test_price_case_with_invalid_price_that_is_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_price_case_with_valid_price_that_is_positive_price(self):
        self.assertEqual(1000, self.robot.price)

    def test_upgrade_case_with_hardware_upgrades_that_has_hardware_component(self):
        self.robot.hardware_upgrades.append('battery')
        self.assertEqual(self.robot.upgrade('battery', 10),
                         "Robot id_1 was not upgraded.")

    def test_upgrade_case_with_empty_hardware_upgrades(self):
        self.assertEqual(self.robot.upgrade('battery', 10),
                         "Robot id_1 was upgraded with battery.")
        self.assertEqual(1015, self.robot.price)

    def test_update_with_available_updates_and_version_less_or_equal_than_max_of_updates_and_not_enough_capacity(self):
        self.robot.software_updates.append(5.0)
        self.assertEqual(self.robot.update(10.0, 150), 'Robot id_1 was not updated.')

        self.assertEqual([5.0], self.robot.software_updates)

        self.robot.software_updates.append(10.0)
        self.assertEqual(self.robot.update(10.0, 150), 'Robot id_1 was not updated.')
        self.assertEqual(self.robot.update(10.0, 50), 'Robot id_1 was not updated.')

        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual([5.0, 10.0], self.robot.software_updates)

        self.robot.available_capacity = 1000
        self.assertEqual(self.robot.update(5.0, 150),
                         'Robot id_1 was not updated.')

        self.assertEqual(1000, self.robot.available_capacity)

    def test_update_with_available_updates_and_version_greater_or_equal_than_max_of_updates_and_enough_capacity(self):
        self.robot.available_capacity = 1000
        self.assertEqual(self.robot.update(10.0, 150),
                         'Robot id_1 was updated to version 10.0.')
        self.robot.software_updates.append(5.0)
        self.assertEqual(self.robot.update(50.0, 150),
                         'Robot id_1 was updated to version 50.0.')

    def test_gt_method_case_with_other_robot_price_less_than_price(self):
        robot2 = Robot('id_2', 'Humanoids', 100, 500)
        robot3 = Robot('id_3', 'Humanoids', 100, 100)

        self.assertEqual(robot2.__gt__(robot3),
                         'Robot with ID id_2 is more expensive than Robot with ID id_3.')

    def test_gt_method_case_with_equality_in_prices(self):
        robot2 = Robot('id_2', 'Humanoids', 100, 1000)
        self.assertEqual(self.robot.__gt__(robot2),
                         'Robot with ID id_1 costs equal to Robot with ID id_2.')

    def test_gt_method_case_with_other_robot_price_greater_than_price(self):
        robot2 = Robot('id_2', 'Humanoids', 100, 100)
        robot3 = Robot('id_3', 'Humanoids', 100, 500)

        self.assertEqual(robot2.__gt__(robot3),
                         'Robot with ID id_2 is cheaper than Robot with ID id_3.')


if __name__ == '__main__':
    main()
