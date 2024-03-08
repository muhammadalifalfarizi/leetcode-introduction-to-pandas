import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[
        animals['weight'] > 100
    ].sort_values(
        ['weight'], ascending=False
    )[['name']]

animals_data = pd.DataFrame({
    'name' : ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species' : ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age' : [98, 50, 6, 45, 100, 26],
    'weight' : [464, 41, 328, 463, 50, 349]
})

print(animals_data)
print('\n')
result = findHeavyAnimals(animals_data)
print(result)

'''
Short Answer
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[
        animals['weight'] > 100
    ].sort_values(
        ['weight'], ascending=False
    )[['name']]
'''