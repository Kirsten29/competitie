import unittest
from game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game1 = Game(
            home = 'GRO',
            away = 'EMM',
            score = '2-1'
        )
        self.game2 = Game(
            home = 'GRO',
            away = 'EMM',
            score = '0-1'
        )
        self.game3 = Game(
            home = 'GRO',
            away = 'HEE',
            score = '2-2'
        )

    def test_init(self):
        self.assertEqual(self.game1.home, 'GRO')
        self.assertEqual(self.game1.away_goals, 1)

    def test_winner(self):
        self.assertEqual(self.game1.winner(), 'GRO')
        self.assertEqual(self.game2.winner(), 'EMM')
        self.assertIsNone(self.game3.winner())


    def test_result(self):
        self.assertEqual(self.game1.points('GRO'), 3)
        self.assertEqual(self.game1.points('EMM'), 0)
        self.assertEqual(self.game3.points('GRO'), 1)

