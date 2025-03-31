import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Apply string title case formatting to the 'name' column
    users["name"] = users["name"].str.capitalize()
    
    # Sort by user_id
    return users.sort_values(by="user_id").reset_index(drop=True)