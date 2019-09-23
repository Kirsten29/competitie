class Game:

    def __init__(self, home, away, score):
        self.home = home
        self.away = away
        goals = score.split('-')
        self.home_goals, self.away_goals = int(goals[0]), int(goals[1])

    def winner(self):
        if self.home_goals > self.away_goals:
            return self.home
        elif self.home_goals < self.away_goals:
            return self.away
        else:
            return None

    def points(self, team):
        winner = self.winner()
        if winner:
            if winner == team:
                return 3
            else:
                return 0
        else:
            return 1
