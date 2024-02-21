import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], var_name='quarter', value_name='sales')


report_data = pd.DataFrame({
    'product' : ['Umbrella', 'SleepingBag'],
    'quarter_1' : [417, 800],
    'quarter_2' : [224, 936],
    'quarter_3' : [379, 93],
    'quarter_4' : [611, 875]
})

print(report_data)
print('\n')
result = meltTable(report_data)
print(result)

'''
Short Answer
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], var_name='quarter', value_name='sales')
'''