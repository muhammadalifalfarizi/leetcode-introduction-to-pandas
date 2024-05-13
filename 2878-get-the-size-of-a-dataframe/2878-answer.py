import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

data = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabela', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['Real Madrid', 'Barcelona', 'Manchester United', 'Liverpool', 'Bayern Munich',
             'Chelsea', 'Juventus', 'Paris Saint-Germain', 'Manchester City', 'Arsenal']
}

players_df = pd.DataFrame(data)
result = getDataframeSize(players_df)
print(result)

'''
Short Answer
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
'''