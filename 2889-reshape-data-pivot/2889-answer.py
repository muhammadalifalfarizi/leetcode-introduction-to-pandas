import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

weather_data = pd.DataFrame({
    'city' : ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'El Paso', 'El Paso', 'El Paso', 'El Paso', 'El Paso'],
    'month' : ['January', 'February','March', 'April', 'May', 'January', 'February', 'March','April', 'May'],
    'temperature' : [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
})

result = pivotTable(weather_data)
print(result)

'''
Short Answer
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
'''