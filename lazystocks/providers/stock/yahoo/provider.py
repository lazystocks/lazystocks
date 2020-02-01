def get_raw_data(stock="SPY"):
    data = yf.Ticker(stock)
    print(data)
    return data


def transform_df_to_normal_form():
    pass


def get_df():
    data = get_raw_data()
    return transform_df_to_normal_form(data)
