import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate bonus using conditions
    employees["bonus"] = employees.apply(lambda x: x["salary"] if x["employee_id"] % 2 != 0 and not x["name"].startswith('M') else 0, axis=1)
    
    # Select required columns and sort by employee_id
    result = employees[["employee_id", "bonus"]].sort_values(by="employee_id")