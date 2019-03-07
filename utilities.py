# -*- coding: utf-8 -*-
import hashlib
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import namedtuple

CF_Row = namedtuple('CF_Row', 'DATE IN OUT NET')

def gen_key(email, positions):
    print str(positions)
    return hashlib.sha256(email + str(positions)).hexdigest()


def invalid_request():
    res = dict()
    res['message'] = 'invalid request'

    return res
# print gen_key('minikie2@naver.com', '{test:test,test1:test1}2')

def send_email(email, access_key):
    pass


def cashflow_merge(positions):
    cf = pd.DataFrame()

    return cf


def test():
    # http://www.macquarie.com/kr/kr/acrobat/m_nps_reit_mltm_quarterly_investment_report_300608.pdf
    current_value = 0

    df = pd.DataFrame.from_dict(json_normalize(position_items), orient='columns')

    asset = sum(current_values)
    liability = sum(depts) #
    liability_ratio = sum(depts) / asset
    capital = asset - liability
    book_value = sum(book_values)
    position_count = count(positions)
    owner_position_count = count(positions)
    rent_position_count = count(positions)

    # projection periods : 5Y
    projection_periods = 5
    projection_month_count = projection_periods * 12

    report_date = datetime.today()

    year = report_date.year
    month = report_date.month
    day = report_date.day

    dates = []
    inflows = []
    outflows = []
    report_date.date()
    for i in range(projection_month_count):
        date_after_month = report_date + relativedelta(months=i)
        d_str = date_after_month.strftime('%Y-%m-%d')
        dates.append(d_str)

        # [p. for p in position_items]
        inflows.append()
        outflows.append(float(df['book_value'].sum()))




# 구분
# 법정동 : legal_dong
# 아파트 : apt_name
# 전용면적 : private_area
# 지역코드 : region_code
def calculate_price(position):
    res = dict()

    res['trade_type'] = 'rent'
    res['price'] = 30000
    res['monthly_payment'] = 0
    res['reserve_amount'] = 10000
    res['trade_price'] = 30000

    return res


# json_string = '''
# [{u'name': u'test name1', u'position_type': u'owner_occupied', u'loan': {u'effective_date': u'2018-10-11', u'amount': 0, u'type': u'fixed', u'rate': 0.03, u'maturity_date': u'2018-10-11'}, u'address': u'test address', u'hasLoan': False, u'rent': {u'effective_date': u'2018-10-11', u'monthly_payment': 1000, u'deposit': 0, u'maturity_date': u'2018-10-11'}, u'book_date': u'2018-10-11', u'book_value': 10000}, {u'name': u'test name2', u'position_type': u'owner_occupied', u'loan': {u'effective_date': u'2018-10-11', u'amount': 0, u'type': u'fixed', u'rate': 0.03, u'maturity_date': u'2018-10-11'}, u'address': u'test address', u'hasLoan': False, u'rent': {u'effective_date': u'2018-10-11', u'monthly_payment': 1000, u'deposit': 0, u'maturity_date': u'2018-10-11'}, u'book_date': u'2018-10-11', u'book_value': 10000}]
# '''
#
# import json
# print json.loads(json_string)
if __name__ == '__main__':
    cf11 = CF_Row('2018-10-11', 100, 110, -10)
    cf12 = CF_Row('2018-11-11', 200, 210, -10)

    cfs1 = [cf11, cf12]
    df1 = pd.DataFrame(cfs1)
    df1.set_index('DATE')


    cf21 = CF_Row('2018-11-11', 100, 110, -10)
    cf22 = CF_Row('2018-12-11', 200, 210, -10)

    cfs2 = [cf21, cf22]
    df2 = pd.DataFrame(cfs2)
    df2.set_index('DATE')

    #print (df1.append(df2)).groupby('DATE').sum().to_json(orient='split')
    df = (df1.append(df2)).groupby('DATE').sum()
    # print df.to_json(orient='split')
    # print df.to_json(orient='index')
    # print df.to_json(orient='records')
    # print df.to_json(orient='columns')
    from flask import jsonify

    print df['IN']


    # import numpy as np
    # take_smaller = lambda s1, s2: s1+s2
    # print df1.combine(df2, take_smaller)