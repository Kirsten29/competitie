import csv

from game import Game
from team import Team

class Competition:
    
    def __init__(self, filename):
        self.games = []
        self.teams = dict()
        self.read(filename)

    def read(self, filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                game = Game(**row)
                self.games.append(game)
                for team_name in [game.home, game.away]:
                    if team_name not in self.teams:
                        self.teams[team_name] = Team(team_name)

    def process(self):
        for game in self.games:
            self.teams[game.home].process_game(game)
            self.teams[game.away].process_game(game)
            