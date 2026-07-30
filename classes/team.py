class Team():
    def __init__(self, name, players,  fan_satisfaction, ):
        self.name = name
        self.players = players
        self.budget = 500
        self.fan_satisfaction = fan_satisfaction

    def buy_player(self, player):
        self.players.append(player)

    def sell_player(self, player):
        self.players.remove(player)

    def resize_fan_satisfaction(self, value):
        self.fan_satisfaction += value