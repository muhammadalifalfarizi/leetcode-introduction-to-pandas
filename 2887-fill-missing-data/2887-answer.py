import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

data = pd.DataFrame(
    {'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
     'quantity': [None, None, 779, 849],
     'price' : [135, 821, 9319, 3051]}
)

print(data)
print('\n')
products_df = fillMissingValues(data)
print(products_df)

'''
Short Answer
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
'''