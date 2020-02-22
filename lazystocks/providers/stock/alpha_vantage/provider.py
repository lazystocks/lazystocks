import requests
import pandas as pd
import re


def url(api_key, symbol):
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="+symbol+"&apikey="+api_key


def get_raw_data(api_key, symbol):
    res = requests.get(url=url(api_key, symbol)).json()
    return res


def transform_data_to_df_normal_form(data):
    daily_data = data["Time Series (Daily)"]
    df = pd.DataFrame(daily_data)
    df = df.T #each row should be a sample
    remove_numbers_and_spaces = lambda s:re.sub("(\d*)([\.]*)(\s*)", "", s)
    df = df.rename(remove_numbers_and_spaces, axis='columns')
    # TODO: clean and transform to normal form
    return df


def get_df(api_key, symbol="SPY"):
    data = get_raw_data(api_key, symbol)
    return transform_data_to_df_normal_form(data)
