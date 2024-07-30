from project.mammal import Mammal


from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Iza', 'cat', 'meow')

    def testing_initialization(self):
        self.assertIsInstance(self.mammal, Mammal)
        self.assertEqual('Iza', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def testing_make_sound_method(self):
        result = self.mammal.make_sound()
        self.assertEqual("Iza makes meow", result)

    def testing_get_kingdom_method(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def testing_get_info_method(self):
        result = self.mammal.info()
        self.assertEqual("Iza is of type cat", result)


if __name__ == '__main__':
    main()
