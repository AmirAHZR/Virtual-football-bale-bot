import json
from typing import List


class Player:
    def __init__(self, name: str, post: str):
        self.name = name
        self.post = post

    def __repr__(self):
        return self.name


class Club:
    def __init__(self, name: str, players: List[Player] = None):
        self.name = name
        self.players = players if players else []

    def get_players_by_position(self, post: str) -> List[str]:
        
        return [p.name for p in self.players if post.lower() in p.post.lower()]

    def show_squad(self):
        print(f"\n{'='*40}")
        print(f"  {self.name}")
        print(f"{'='*40}")
        for player in self.players:
            print(player.name)

    def __repr__(self):
        return f"Club({self.name}, {len(self.players)} players)"


def load_clubs(filename) -> dict[str, Club]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    clubs = {}
    for club_name, players_data in data.items():
        players = [
            Player(name=p["نام"], post=p["پست"])
            for p in players_data
        ]
        clubs[club_name] = Club(club_name, players)

    return clubs

clubs = load_clubs("squads.json")