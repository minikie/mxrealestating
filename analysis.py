# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from pandas.io.json import json_normalize
from utilities import CF_Row


class PositionItem:
    def __init__(self):
        pass

    def get_cashflow(self, report_date, end_date):
        pass


class Loan(PositionItem):
    def __init__(self, args):
        PositionItem.__init__(self)
        self.amount = args['amount']
        self.rate = args['rate']

    def get_cashflow(self, report_date, end_date):
        roop_date = report_date
        cashflows = []

        while (roop_date <= end_date):
            roop_date = roop_date + relativedelta(months=1)
            d_str = roop_date.strftime('%Y-%m-%d')
            coupon = self.amount * self.rate / 12.0 # monthly payment
            cashflows.append(CF_Row(d_str, 0.0, coupon, coupon))

        return pd.DataFrame(cashflows)


class Rent(PositionItem):
    def __init__(self, args):
        PositionItem.__init__(self)
        self.maturity_date = args['maturity_date']
        self.monthly_payment = args['monthly_payment']

    def get_cashflow(self, report_date, end_date):
        roop_date = report_date
        cashflows = []

        while (roop_date <= end_date):
            roop_date = roop_date + relativedelta(months=1)
            d_str = roop_date.strftime('%Y-%m-%d')
            cashflows.append(CF_Row(d_str, self.monthly_payment, 0.0, self.monthly_payment))

        return pd.DataFrame(cashflows)


class Apartment(PositionItem):
    def __init__(self, args):
        PositionItem.__init__(self)
        self.name = args['name']
        self.address = args['address']
        self.loan = Loan(args['loan'])
        self.rent = Rent(args['rent'])


    def get_cashflow(self, report_date, end_date):
        roop_date = report_date.date()

        loan_cf = self.loan.get_cashflow(report_date, end_date)
        rent_cf = self.rent.get_cashflow(report_date, end_date)

        return loan_cf.append(rent_cf)


def positionitem_factory(args):
    p_type = args['asset_type']
    if p_type == 'apartment':
        return Apartment(args)
    else:
        raise Exception('unknown position type')


# 최신 데이터..?
def get_trade_price(position_item, yyyymm):
    # db 에서 물어옴
    return


def position_analysis(position_items):
    def position_cf_mapping(position_obj_list, report_date, end_date):
        roop_date = report_date
        base_cashflows = []

        while (roop_date <= end_date):
            roop_date = roop_date + relativedelta(months=1)
            d_str = roop_date.strftime('%Y-%m-%d')
            base_cashflows.append(CF_Row(d_str, 0.0, 0.0, 0.0))

        base_cashflows_df = pd.DataFrame(base_cashflows)

        for p in position_obj_list:
            position_obj = positionitem_factory(p)
            p_df = position_obj.get_cashflow(result_date, end_date)
            base_cashflows_df = base_cashflows_df.append(p_df)

        return base_cashflows_df.groupby('DATE').sum()


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
    result_date = datetime.datetime.today()
    end_date = result_date + relativedelta(years=5)

    results_data = dict()
    results_data['result_date'] = result_date.strftime('%Y-%m-%d')
    results_data['timestamp'] = timestamp = str(datetime.datetime.utcnow())

    summary = dict()
    summary['asset_amount'] = float(df['book_value'].sum())
    summary['liability_amount'] = float(df['book_value'].sum())
    summary['capital_amount'] = float(df['book_value'].sum())

    summary['profit_percent'] = float(df['book_value'].sum())
    summary['profit_amount'] = float(df['book_value'].sum())

    results_data['summary'] = summary

    result_df = position_cf_mapping(position_items, result_date, end_date)

    flows = dict()
    flows['dates'] = result_df.index.tolist()
    flows['inflows'] = result_df['IN'].tolist()
    flows['outflows'] = result_df['OUT'].tolist()

    results_data['flows'] = flows

    res['results_data'] = results_data

    return res


if __name__ == '__main__':
    print ('------------------------test-------------------------')

    json_str = '''{
        "position_list": [
            {
                "name": "test name1",
                "asset_type": "apartment",
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
                    "amount": 10000,
                    "type":"fixed",
                    "rate": 0.03,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                }
            },
            {
                "name": "test name2",
                "asset_type": "apartment",
                "address": "test address",
                "book_value": 10000,
                "book_date": "2018-10-11",
                "position_type": "owner_occupied",
                "rent": {
                    "deposit": 0,
                    "monthly_payment": 300,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                },
                "hasLoan": false,
                "loan": {
                    "amount": 20000,
                    "type":"fixed",
                    "rate": 0.03,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                }
            }
        ]
        }
    '''

    # import json    # or `import simplejson as json` if on Python < 2.6

    # obj = json.loads(json_str)
    # print position_analysis(obj['position_list'])
