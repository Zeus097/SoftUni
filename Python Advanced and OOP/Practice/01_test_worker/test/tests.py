from project.worker import Worker


# For Judge - everything below...
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 1000, 100)

    def test_instantiation(self):
        self.assertEqual(self.worker.name, 'Ivan')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)
        self.assertTrue(self.worker.money == 0)

    def test_energy_incrementation_after_rest_method_is_called(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

        self.worker.energy = 200
        self.worker.rest()
        self.assertEqual(self.worker.energy, 201)

    def test_worker_if_error_is_raised_if_work_with_negative_energy_or_equal_to_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_who_is_working_with_positive_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)
        self.assertEqual(self.worker.energy, 99)

        self.worker.work()
        self.assertEqual(self.worker.money, 2000)
        self.assertEqual(self.worker.energy, 98)

        self.worker.money = 0
        self.worker.energy = 100
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_method_returns_correct_information(self):
        self.worker.get_info()
        result = self.worker.get_info()
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', result)


if __name__ == '__main__':
    main()
