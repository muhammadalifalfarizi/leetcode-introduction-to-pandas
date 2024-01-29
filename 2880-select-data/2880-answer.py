import pandas as pd
from typing import List

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    result = students[students['student_id'] == 101][['name', 'age']]

    return result


students_data = pd.DataFrame({
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
})

result_df = selectData(students_data)
print(result_df)

'''
Short Answer
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name','age']] or
    return students[students.student_id == 101][["name", "age"]]
'''