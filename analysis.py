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

    loan = dict()
    loan['amount'] = 20000
    rent = dict()
    rent['deposit'] = 20000

    res['book_value'] = float(df['book_value'].sum())
    res['loan'] = loan
    res['rent'] = rent

    res['result_date'] = '2018-10-11'
    res['profit_percent'] = 0.2
    res['profit_amount'] = 0.2

    return res