import unittest

from game import Game
from team import Team

class TeamTest(unittest.TestCase):

    def setUp(self):
        self.team = Team('GRO')

    def test_init(self):
        self.assertEqual(self.team.name, 'GRO')
        self.assertEqual(self.team.points, 0)
        self.assertEqual(self.team.goals, 0)
        self.assertEqual(self.team.goals_against, 0)
        self.assertEqual(self.team.saldo(), 0)
    
    def test_game(self):
        game = Game(
            home='GRO',
            away='EMM',
            score='2-1'
        )
        self.team.process_game(game)

        self.assertEqual(self.team.name, 'GRO')
        self.assertEqual(self.team.points, 3)
        self.assertEqual(self.team.goals, 2)
        self.assertEqual(self.team.goals_against, 1)
        self.assertEqual(self.team.saldo(), 1)

        game = Game(
            home='GRO',
            away='HEE',
            score='2-2'
        )
        self.team.process_game(game)
        self.assertEqual(self.team.points, 4)
        self.assertEqual(self.team.goals, 4)
        self.assertEqual(self.team.goals_against, 3)
        self.assertEqual(self.team.saldo(), 1)
