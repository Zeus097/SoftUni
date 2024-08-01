from project.tennis_player import TennisPlayer


from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player1 = TennisPlayer('John', 25, 100.00)
        self.player2 = TennisPlayer('Ivan', 30, 200.00)
        self.player3 = TennisPlayer('Niki', 35, 300.00)
        self.player3.add_new_win('World cup')
        self.player3.add_new_win('Player of the year')

    def test_initialisation(self):
        self.assertIsInstance(self.player1, TennisPlayer)
        self.assertEqual('John', self.player1.name)
        self.assertEqual(25, self.player1.age)
        self.assertEqual(100.00, self.player1.points)
        self.assertEqual([], self.player1.wins)

    def test_name_validation_with_not_enough_letters(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('Jo', 25, 100.00)
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_age_validation_case_when_age_is_below_the_needed_value(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer('John', 17, 100.00)
        self.assertEqual(str(ve.exception), 'Players must be at least 18 years of age!')

    def test_add_new_win_method_with_not_existing_tournament_name(self):
        self.player1.add_new_win('Final Tournament')
        self.assertEqual(self.player1.wins, ['Final Tournament'])

    def test_add_new_win_method_with_existing_tournament_name(self):
        self.player1.wins.append('Final Tournament')
        self.assertEqual(self.player1.add_new_win('Final Tournament'),
                         'Final Tournament has been already added to the list of wins!')

    def test_lt_method(self):
        self.assertEqual(self.player1.__lt__(self.player2),
                         'Ivan is a top seeded player and he/she is better than John')
        self.assertEqual(self.player3.__lt__(self.player2), 'Niki is a better player than Ivan')

    def test_str_method(self):
        self.assertEqual(str(self.player3), "Tennis Player: Niki\n"
                                            "Age: 35\n"
                                            "Points: 300.0\n"
                                            "Tournaments won: World cup, Player of the year")


if __name__ == '__main__':
    main()
