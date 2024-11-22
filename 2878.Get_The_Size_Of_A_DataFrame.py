
from typing import List
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Get the number of rows and columns in the DataFrame
    rows = players.shape[0]
    columns = players.shape[1]
    
    # Return the result as a list
    return [rows, columns]

# Example Usage
if __name__ == "__main__":
    # Sample DataFrame
    data = {
        "player_id": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
        "name": ["Mason", "Riley", "Bob", "Isabella", "Zachary", "Ava", "Violet", "Thomas", "Jack", "Charlie"],
        "age": [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
        "position": ["Forward", "Winger", "Striker", "Goalkeeper", "Midfielder", "Defender", "Striker", "Striker", "Midfielder", "Center-back"],
        "team": ["RealMadrid", "Barcelona", "ManchesterUnited", "Liverpool", "BayernMunich", "Chelsea", "Juventus", "ParisSaint-Germain", "ManchesterCity", "Arsenal"]
    }
    
    players = pd.DataFrame(data)
    
    # Call the function
    print(getDataframeSize(players))  # Output: [10, 5]
