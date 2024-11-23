import pandas as pd
from typing import List

def displayFirstThreeRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Displays the first three rows of the given DataFrame.
    """
    return employees.head(3)

# Example Usage
if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        "employee_id": [3, 90, 9, 60, 49, 43],
        "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
        "department": ["Operations", "Sales", "Engineering", "InformationTechnology", "HumanResources", "Administration"],
        "salary": [48675, 11096, 33805, 37678, 23793, 40454],
    }
    employees = pd.DataFrame(data)

    # Display the first three rows
    result = displayFirstThreeRows(employees)
    print(result)
