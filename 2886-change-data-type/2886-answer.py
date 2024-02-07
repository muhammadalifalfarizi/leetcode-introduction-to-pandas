import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

data = pd.DataFrame(
    {'student_id': [1, 2],
     'name': ['Ava', 'Kate'],
     'age': [6, 15],
     'grade': [73.0, 87.0]}
    )

print(data)
print('\n')
students_df = changeDatatype(data)
print(students_df)

'''
Short Answer
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
'''



