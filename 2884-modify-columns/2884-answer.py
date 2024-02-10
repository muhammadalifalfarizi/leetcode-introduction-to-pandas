import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees

employees = pd.DataFrame({
    'name': ['Jack','Piper','Mia','Ulysses'],
    'salary': [19666,74754,62509,54866]
})

new_df = modifySalaryColumn(employees)
print(employees)
print("\n")
print(new_df)

'''
Short Answer
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees
'''

