import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

employees_input = pd.DataFrame({'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
                                'salary': [4548, 28150, 1103, 6593, 74576, 24433]})

result_df = createBonusColumn(employees_input)
print(result_df)

'''
Short Answer
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
'''