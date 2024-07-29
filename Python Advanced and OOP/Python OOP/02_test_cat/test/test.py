from project.cat import Cat


from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Izabel')

    def test_cat_initialization(self):
        self.assertIsInstance(self.cat, Cat)
        self.assertEqual(self.cat.name, 'Izabel')
        self.assertFalse(self.cat.fed, False)
        self.assertFalse(self.cat.sleepy, False)
        self.assertEqual(self.cat.size, 0)

    def testing_eat_case_when_cat_is_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))
        self.assertEqual(self.cat.size, 0)

    def testing_eat_case_when_cat_is_not_fed(self):
        self.cat.fed = False
        self.cat.eat()
        self.assertTrue(self.cat.fed, True)
        self.assertTrue(self.cat.sleepy, True)
        self.assertEqual(self.cat.size, 1)

    def testing_sleep_case_when_cat_is_not_fed(self):
        self.cat.fed = False
        self.cat.sleepy = True

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertTrue(self.cat.sleepy, True)
        self.assertFalse(self.cat.fed, False)

    def testing_sleep_case_when_cat_is_fed(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy, False)
        self.assertTrue(self.cat.fed, True)


if __name__ == '__main__':
    main()
