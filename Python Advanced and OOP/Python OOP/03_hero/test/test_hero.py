from project.hero import Hero


from unittest import TestCase, main


class TestHero(TestCase):
    username = 'Ivan'
    level = 100
    health = 100
    damage = 100

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_initialization(self):
        self.assertIsInstance(self.hero, Hero)
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_atributes_type(self):
        self.assertTrue(self.hero.username, str)
        self.assertTrue(self.hero.level, int)
        self.assertTrue(self.hero.health, float)
        self.assertTrue(self.hero.damage, float)

    def test_hero_username_equals_to_enemy_username_in_battle_method(self):
        enemy = Hero(self.username, 50, 100, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_is_equal_to_zero_in_battle_method(self):
        self.hero.health = 0
        enemy = Hero('Gosho', 50, 100, 50)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_hero_health_is_bellow_zero_in_battle_method(self):
        self.hero.health = -100
        enemy = Hero('Gosho', 50, 100, 50)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_health_is_equal_to_zero_in_battle_method(self):
        enemy = Hero('Gosho', 50, 0, 50)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_enemy_health_is_below_zero_in_battle_method(self):
        enemy = Hero('Gosho', 50, -100, 50)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_draw(self):
        enemy = Hero('Gosho', self.level, self.health, self.damage)
        result = self.hero.battle(enemy)

        self.assertEqual(100, self.hero.level)
        self.assertEqual(-9900, self.hero.health)
        self.assertEqual(100, self.hero.damage)
        self.assertEqual('Draw', result)

    def test_win(self):
        self.hero.health = 100
        enemy = Hero('Gosho', 1, 1, 1)
        result = self.hero.battle(enemy)

        self.assertEqual(101, self.hero.level)
        self.assertEqual(104, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual('You win', result)

    def test_lose(self):
        self.hero.level = 1
        self.hero.health = 1
        self.hero.damage = 1
        enemy = Hero('Gosho', 200, 200, 350)
        result = self.hero.battle(enemy)

        self.assertEqual(201, enemy.level)
        self.assertEqual(204, enemy.health)
        self.assertEqual(355, enemy.damage)
        self.assertEqual('You lose', result)

    def test_str_method(self):
        result = self.hero.__str__()
        self.assertEqual("Hero Ivan: 100 lvl\nHealth: 100\nDamage: 100\n", result)


if __name__ == '__main__':
    main()
