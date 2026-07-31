from main import clubs

squads = {}

for club in clubs:
    club_name = clubs[club]
    players = clubs[club].players
    squads.update({club_name.name: players})

print(squads)
    