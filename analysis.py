# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from pandas.io.json import json_normalize


class PositionItem:
    def __init__(self, **args):
        self.name = args['name']
        self.address = args['address']


def position_analysis(position_items):
    res = dict()

    # dataframe ?
    df = pd.DataFrame.from_dict(json_normalize(position_items), orient='columns')

    print(df)

    #        results_data:{
    #             name: 'not calculated',
    #             result_date: undefined,
    #             summary: {
    #                 asset_amount: 10000, // 현재가
    #                 liability_amount: 10000,
    #                 capital_amount: 10000,
    #
    #                 profit_percent: 0.03,
    #                 profit_amount: 10000
    #             },
    #             flows: {
    #                 dates: ["2018-10-11","2018-10-11"],
#                     inflows: [100,100],
#                     outflows: [100,100]
    #             },
    #             comments: {
    #
    #             }
    #
    #         },

    results_data = dict()
    results_data['result_date'] = "2018-10-11"
    results_data['timestamp'] = timestamp = str(datetime.datetime.utcnow())

    summary = dict()
    summary['asset_amount'] = float(df['book_value'].sum())
    summary['liability_amount'] = float(df['book_value'].sum())
    summary['capital_amount'] = float(df['book_value'].sum())

    summary['profit_percent'] = float(df['book_value'].sum())
    summary['profit_amount'] = float(df['book_value'].sum())

    results_data['summary'] = summary

    flows = dict()
    flows['dates'] = ["2018-10-11", '2018-11-11']
    flows['inflows'] = [100, 100]
    flows['outflows'] = [200, 150]

    results_data['flows'] = flows

    res['results_data'] = results_data

    return res


if __name__ == '__main__':
    print ('test')

    json_str = '''{
        "position_list": [
            {
                "name": "test name1",
                "address": "test address",
                "book_value": 10000,
                "book_date": "2018-10-11",
                "position_type": "owner_occupied",
                "rent": {
                    "deposit": 0,
                    "monthly_payment": 1000,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                },
                "hasLoan": false,
                "loan": {
                    "amount": 0,
                    "type":"fixed",
                    "rate": 0.03,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                }
            },
            {
                "name": "test name2",
                "address": "test address",
                "book_value": 10000,
                "book_date": "2018-10-11",
                "position_type": "owner_occupied",
                "rent": {
                    "deposit": 0,
                    "monthly_payment": 1000,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                },
                "hasLoan": false,
                "loan": {
                    "amount": 0,
                    "type":"fixed",
                    "rate": 0.03,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                }
            }
        ]
        }
    '''

    import json    # or `import simplejson as json` if on Python < 2.6

    obj = json.loads(json_str)
    print position_analysis(obj['position_list'])