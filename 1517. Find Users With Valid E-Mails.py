import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define the regex pattern for a valid email
    email_pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    
    # Filter valid emails using the regex pattern
    valid_users = users[users["mail"].str.match(email_pattern, na=False)]
    
    return valid_users