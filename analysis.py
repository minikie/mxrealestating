import pandas as pd
from pandas.io.json import json_normalize

class PositionItem:
    def __init__(self, notional, lent_type):
        self.notional = notional
        self.lent_type = lent_type


def position_analysis(position_items):
    res = dict()

    # dataframe ?
    df = pd.DataFrame.from_dict(json_normalize(position_items), orient='columns')

    res['total_book_value'] = float(df['book_value'].sum())
    print res['total_book_value']
    res['total_profit'] = 0.1
    res['total_notional_amount'] = 0.1
    res['total_eval'] = 0.1

    return res