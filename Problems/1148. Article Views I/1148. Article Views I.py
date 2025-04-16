import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id is equal to viewer_id
    result = views[views["author_id"] == views["viewer_id"]][["author_id"]]
    
    # Drop duplicates to get unique author IDs
    result = result.drop_duplicates()
    
    # Rename column as required and sort the result
    result.columns = ["id"]
    result = result.sort_values(by="id").reset_index(drop=True)
    
    return result