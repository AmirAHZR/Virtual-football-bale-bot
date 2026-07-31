from pickle import load

with open("pkls/squads.pkl", "rb") as f:
    squads = load(f)

print(squads)

    
