import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filtering the big countries based on the given conditions
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Selecting required columns
    return big_countries_df[['name', 'population', 'area']]