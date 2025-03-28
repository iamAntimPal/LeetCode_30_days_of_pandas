import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets where content length is greater than 15
    result = tweets[tweets["content"].str.len() > 15][["tweet_id"]]
    
    return result