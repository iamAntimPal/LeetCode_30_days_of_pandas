import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select customers whose id is not in orders' customerId
    result = customers[~customers["id"].isin(orders["customerId"])][["name"]]
    
    # Rename column as required
    result.columns = ["Customers"]
    
    return result