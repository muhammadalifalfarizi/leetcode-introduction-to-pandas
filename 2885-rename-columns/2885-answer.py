import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={
            'id': 'student_id',
            'first': 'first_name',
            'last': 'last_name',
            'age': 'age_in_years'})
    return students


students_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
})

print(students_df)
print('\n')
df = renameColumns(students_df)
print(df)

'''
Short Answer
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            'id': 'student_id',
            'first': 'first_name',
            'last': 'last_name',
            'age': 'age_in_years'
        }
    )
    return students
'''