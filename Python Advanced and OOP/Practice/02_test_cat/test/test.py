from project.cat import Cat


# For Judge...
from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_init(self):
        self.assertIsInstance(self.cat, Cat)
        self.assertEqual(self.cat.name, 'Tom')
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_already_fed_case(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))
        self.assertEqual(self.cat.size, 0)

    def test_increasing_size_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, 1)

    def test_cannot_sleep_while_hungry_case(self):
        self.cat.sleepy = True
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertTrue(self.cat.sleepy)
        self.assertFalse(self.cat.fed)

    def test_sleep_case_after_is_fed(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)
        self.assertTrue(self.cat.fed)


if __name__ == '__main__':
    main()
