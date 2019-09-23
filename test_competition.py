import unittest
from competition import Competition


class CompetitionTest(unittest.TestCase):
    
    def setUp(self):
        self.competition = Competition('fixture1.csv')

    def test_init(self):
        self.assertEqual(len(self.competition.games), 3)
        self.assertEqual(len(self.competition.teams.keys()), 3)

    def test_processing(self):
        self.competition.process()
        self.assertEqual(len(self.competition.teams), 3)
        gro = self.competition.teams['GRO']
        self.assertEqual(gro.points, 4)
        self.assertEqual(gro.goals, 3)
        self.assertEqual(gro.goals_against, 3)
        self.assertEqual(gro.saldo(), 0)
        