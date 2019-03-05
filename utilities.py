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
    for i in range(projection_month_count):
        date_after_month = report_date + relativedelta(months=i)
        d_str = date_after_month.strftime('%Y-%m-%d')
        dates.append(d_str)

        [p. for p in position_items]
        inflows.append()
        outflows.append(float(df['book_value'].sum()))




