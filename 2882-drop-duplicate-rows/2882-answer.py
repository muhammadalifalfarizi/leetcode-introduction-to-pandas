import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(['email'])

customers = pd.DataFrame({
    'customer_id' : [1,2,3,4,5,6],
    'name' : ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    'email' : ["emily@example.com", "michael@example.com", "sarah@example.com",
               "john@example.com", "john@example.com", "alice@example.com"]
})

result = dropDuplicateEmails(customers)
print(customers)
print("\n")
print(result)

'''
Short Answer
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(['email'])
'''