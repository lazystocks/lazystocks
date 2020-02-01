import requests
import pandas as pd


def url(api_key, symbol):
    return "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="+symbol+"&apikey="+api_key


def get_raw_data(api_key, symbol="SPY"):
    res = requests.get(url=url(api_key, symbol)).json()
    print(res)
    return res


def transform_data_to_df_normal_form(data):
    df = pd.DataFrame(data)
    # TODO: cleand and transform to normal form
    return df


def get_df():
    data = get_raw_data(api)
    return transform_df_to_normal_form(data)
