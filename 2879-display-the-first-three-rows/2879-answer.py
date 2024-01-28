import pandas as pd
from typing import List

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.head(3)
    return result


data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(data)
print("Original DataFrame:")
print(employees)

result_df = selectFirstRows(employees)
print("\nFirst 3 Rows:")
print(result_df)

'''
Short Answer
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
'''