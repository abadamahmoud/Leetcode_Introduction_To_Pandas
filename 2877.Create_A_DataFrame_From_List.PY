import pandas as pd
from typing import List

# Function to create DataFrame from student_data
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df

# Example usage
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Create the DataFrame
df = createDataframe(student_data)

# Display the DataFrame
print(df)
