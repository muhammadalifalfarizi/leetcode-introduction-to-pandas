import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    result = students.replace('None', pd.NA).dropna(subset=['name'])
    return result

students = pd.DataFrame({
    'student_id' : [32, 217, 779, 849],
    'name' : ['Piper', 'None', 'Georgia', 'Willow'],
    'age' : [5, 19, 20, 14]
})

result_df = dropMissingData(students)
print(result_df)

'''
Short Answer
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
'''

