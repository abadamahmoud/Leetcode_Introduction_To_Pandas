import pandas as pd

def selectStudentData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where student_id is 101 and select only name and age columns
    result = students.loc[students['student_id'] == 101, ['name', 'age']]
    return result

# Example usage:
data = {
    "student_id": [101, 53, 128, 3],
    "name": ["Ulysses", "William", "Henry", "Henry"],
    "age": [13, 10, 6, 11]
}

students = pd.DataFrame(data)
print(selectStudentData(students))
