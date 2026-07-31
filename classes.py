from typing import List


class Player:
    def __init__(self, name: str, post: str):
        self.name = name
        self.post = post

    
class Club:
    def __init__(self, fan, budget,name: str, players: List[Player] = None):
        self.name = name
        self.fan = fan
        self.budget = budget
        self.players = players if players else []


