from project.worker import Worker


from unittest import TestCase, main


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 1000, 100)

    def test_initialization(self):
        self.assertIsInstance(self.worker, Worker)
        self.assertEqual(self.worker.name, 'Ivan')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)

    def testin_case_when_energy_is_equal_to_zero(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def testin_case_when_energy_is_below_zero(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def testin_case_when_energy_is_above_zero(self):
        self.worker.energy = 100
        self.worker.money = 0

        self.worker.work()

        self.assertEqual(self.worker.money, self.worker.salary)
        self.assertEqual(self.worker.energy, 99)

    def testing_the_rest_process(self):
        self.worker.energy = 99
        self.worker.rest()

        self.assertEqual(self.worker.energy, 100)

    def testing_get_info(self):
        self.worker.money = 2000
        expected = 'Ivan has saved 2000 money.'
        self.worker.get_info()

        self.assertEqual(expected, self.worker.get_info())


if __name__ == '__main__':
    main()
