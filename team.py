class Team:
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals = 0
        self.goals_against = 0

    def process_points(self, game):
        self.points += game.points(self.name)

    def process_goals(self, game):
        if self.name == game.home:
            self.goals += game.home_goals
            self.goals_against += game.away_goals
        else:
            self.goals += game.away_goals
            self.goals_against += game.home_goals

    def process_game(self, game):
        self.process_points(game)
        self.process_goals(game)

    def saldo(self):
        return self.goals - self.goals_against
