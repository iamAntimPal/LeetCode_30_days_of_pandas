import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter products that are both low fat ('Y') and recyclable ('Y')
    result = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]

    # Select only the product_id column
    return result[["product_id"]]