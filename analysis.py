# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from module.models import TradePrice
from module.database import db_session, init_db
from dateutil.relativedelta import relativedelta
from pandas.io.json import json_normalize
from utilities import CF_Row
import xml.etree.ElementTree as ET
import requests
import json # or `import simplejson as json` if on Python < 2.6

#api_key = 'Oh7DEmB%2FqCK%2BnQvU5VEpBpwmy7UHaZSUrvRl8LTlL0AuCaxTD5yFlaZUUTYQgUxwAUqweyWeFJF6zB3qCswM7w%3D%3D'
api_key = 'Oh7DEmB%2FqCK%2BnQvU5VEpBpwmy7UHaZSUrvRl8LTlL0AuCaxTD5yFlaZUUTYQgUxwAUqweyWeFJF6zB3qCswM7w%3D%3D'


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


# 이거는 raw 데이터
def download_trade_price(region_code, yyyymm):
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    parameters = '?' + 'serviceKey=' + api_key +'&pageNo=1&numOfRows=1000&LAWD_CD=' + str(region_code) + '&DEAL_YMD=' + str(yyyymm)
    res = requests.get(url + parameters)
    root = ET.fromstring(res.text)
    timestamp = str(datetime.datetime.utcnow())

    # 지워지나..?
    TradePrice.query.filter(TradePrice.yyyymm == yyyymm).delete()

    for item in root.findall('body/items/item'):
        trade_price = float(item.find('거래금액').text.replace(',', '').strip())
        build_year = int(item.find('건축년도').text)
        trade_year = int(item.find('년').text)
        apt_name = item.find('아파트').text
        trade_month = int(item.find('월').text)
        trade_days = item.find('일').text # 1~10 , 11~20 , 21~31 ?
        private_area = float(item.find('전용면적').text)
        region_code = item.find('지역코드').text
        floor = int(item.find('층').text)

        tp = TradePrice(yyyymm, trade_price,build_year,trade_year,apt_name,
                        trade_month,trade_days,private_area,region_code,floor,timestamp)

        db_session.add(tp)

    db_session.commit()


# 최신 데이터..?
#def get_trade_price(position_item, yyyymm):
def append_trade_price(df, date):
    yyyymm = date.strftime('%Y%m')
    trade_year = date.year
    trade_month = date.month

    for i in df.index:
        region_code = df.at[i, 'region_code']
        private_area = df.at[i, 'private_area']

        # floor = df.at[i, 'floor']

        tp = TradePrice.query.filter(TradePrice.yyyymm == yyyymm and
                                     TradePrice.region_code == region_code and
                                     TradePrice.private_area.between(private_area-0.5, private_area+0.5)).first()

        # tp = TradePrice.query.filter(TradePrice.yyyymm == yyyymm and
        #                              TradePrice.region_code == region_code,
        #                              TradePrice.private_area.between(private_area-0.5, private_area+0.5)).first()

        if tp is None:
            download_trade_price(region_code, yyyymm)

        # 어떻게 가져올것인가..? 평형 , 거래 날짜 등.
        trades = TradePrice.query.filter(TradePrice.yyyymm == yyyymm and TradePrice.region_code)

        df.at[i, 'trade_price'] = 10000


def make_flow(position_items, report_date, end_date):
    roop_date = report_date
    base_cashflows = []

    while (roop_date <= end_date):
        roop_date = roop_date + relativedelta(months=1)
        d_str = roop_date.strftime('%Y-%m-%d')
        base_cashflows.append(CF_Row(d_str, 0.0, 0.0, 0.0))

    base_cashflows_df = pd.DataFrame(base_cashflows)

    for p in position_items:
        position_obj = positionitem_factory(p)
        p_df = position_obj.get_cashflow(report_date, end_date)
        base_cashflows_df = base_cashflows_df.append(p_df)

    result_df = base_cashflows_df.groupby('DATE').sum()

    res = dict()
    summary = dict()
    summary['inflow_sum'] = result_df['IN'].sum()
    summary['outflow_sum'] = result_df['OUT'].sum()
    summary['net_sum'] = summary['inflow_sum'] - summary['outflow_sum']
    res['summary'] = summary
    res['dates'] = result_df.index.tolist()
    res['inflows'] = result_df['IN'].tolist()
    res['outflows'] = result_df['OUT'].tolist()

    print(res)

    return res


def make_summary(df):
    print('----------------------------------------------------')
    today = datetime.datetime.today()

    append_trade_price(df, today)

    res = dict()

    # 현재 평가를 다 더해야함( 우선은 book_value로 )
    res['asset_amount'] = float(df['trade_price'].sum())

    # print(df[df['position_type']=='자가']['rent.deposit'].sum())
    # print(df.columns)

    # rent + loan -> sum
    rent_sum = float(df[df['position_type']=='자가']['rent.deposit'].sum())
    loan_sum = float(df[df['loan_type'] == '없음']['loan.amount'].sum())
    book_value_sum = float(df['book_value'].sum())

    res['liability_amount'] = rent_sum + loan_sum
    res['capital_amount'] = res['asset_amount'] - res['liability_amount']

    res['profit_amount'] = res['capital_amount'] - book_value_sum
    res['profit_percent'] = res['profit_amount'] / book_value_sum

    return res


def position_analysis(position_items):

    print(position_items)

    res = dict()

    # dataframe ?
    df = pd.DataFrame.from_dict(json_normalize(position_items), orient='columns')

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

    results_data['summary'] = make_summary(df)
    results_data['flows'] = make_flow(position_items, result_date, end_date)

    res['results_data'] = results_data

    return res


# test ------------------------------------------------------------------------------------------------
def test_analysis():
    json_str = '''{
        "position_list": [
            {
                "name": "test name1",
                "asset_type": "apartment",
                "address": "test address",
                "book_value": 10000,
                "book_date": "2018-10-11",
                "private_area": 55.12,
                "region_code": 11110,
                "position_type": "자가",
                "rent": {
                    "deposit": 0,
                    "monthly_payment": 1000,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                },
                "loan_type":"없음",
                "loan": {
                    "amount": 10000,
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
                "private_area": 55.12,
                "region_code": 11210,
                "position_type": "전세",
                "rent": {
                    "deposit": 5000,
                    "monthly_payment": 300,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                },
                "loan_type": "없음",
                "loan_type":"고정금리",
                "loan": {
                    "amount": 3000,
                    "rate": 0.03,
                    "effective_date": "2018-10-11",
                    "maturity_date": "2018-10-11"
                }
            }
        ]
        }
    '''

    obj = json.loads(json_str)
    return position_analysis(obj['position_list'])


def test_trade_price_download():
    region_code = 11110
    yyyymm = 201901
    parameters = {'LAWD_CD': region_code,
                  'DEAL_YMD': yyyymm,
                  'numOfRows': 1000,
                  'serviceKey': api_key}

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    parameters = '?' + 'serviceKey=' + api_key +'&pageNo=1&numOfRows=1000&LAWD_CD=' + str(region_code) + '&DEAL_YMD=' + str(yyyymm)
    print(parameters)
    res = requests.get(url + parameters)
    print(res.text)
    test = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg></header><body><items><item><거래금액>   105,000</거래금액><건축년도>2008</건축년도><년>2019</년><도로명>사직로8길</도로명><도로명건물본번호코드>00004</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>03</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100135</도로명코드><법정동> 사직동</법정동><법정동본번코드>0009</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>11500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>광화문풍림스페이스본(101동~105동)</아파트><월>1</월><일>1~10</일><일련번호>11110-2203</일련번호><전용면적>97.61</전용면적><지번>9</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>   162,000</거래금액><건축년도>2008</건축년도><년>2019</년><도로명>경희궁길</도로명><도로명건물본번호코드>00057</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100010</도로명코드><법정동> 사직동</법정동><법정동본번코드>0009</법정동본번코드><법정동부번코드>0001</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>11500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>광화문풍림스페이스본(106동)</아파트><월>1</월><일>11~20</일><일련번호>11110-2204</일련번호><전용면적>163.33</전용면적><지번>9-1</지번><지역코드>11110</지역코드><층>11</층></item><item><거래금액>   119,000</거래금액><건축년도>2008</건축년도><년>2019</년><도로명>사직로8길</도로명><도로명건물본번호코드>00004</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>03</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100135</도로명코드><법정동> 사직동</법정동><법정동본번코드>0009</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>11500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>광화문풍림스페이스본(101동~105동)</아파트><월>1</월><일>11~20</일><일련번호>11110-2203</일련번호><전용면적>131.44</전용면적><지번>9</지번><지역코드>11110</지역코드><층>13</층></item><item><거래금액>   160,000</거래금액><건축년도>2004</건축년도><년>2019</년><도로명>새문안로3길</도로명><도로명건물본번호코드>00023</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>02</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100158</도로명코드><법정동> 내수동</법정동><법정동본번코드>0073</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>11800</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>경희궁의아침4단지</아파트><월>1</월><일>21~31</일><일련번호>11110-117</일련번호><전용면적>150.48</전용면적><지번>73</지번><지역코드>11110</지역코드><층>14</층></item><item><거래금액>   101,500</거래금액><건축년도>2008</건축년도><년>2019</년><도로명>삼봉로</도로명><도로명건물본번호코드>00095</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>04</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100006</도로명코드><법정동> 견지동</법정동><법정동본번코드>0110</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>12900</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>대성스카이렉스</아파트><월>1</월><일>1~10</일><일련번호>11110-2223</일련번호><전용면적>149.8</전용면적><지번>110</지번><지역코드>11110</지역코드><층>9</층></item><item><거래금액>    20,000</거래금액><건축년도>2017</건축년도><년>2019</년><도로명>대학로</도로명><도로명건물본번호코드>00033</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>00</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100002</도로명코드><법정동> 효제동</법정동><법정동본번코드>0065</법정동본번코드><법정동부번코드>0002</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>16200</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>포레스트힐시티</아파트><월>1</월><일>1~10</일><일련번호>11110-2440</일련번호><전용면적>16.672</전용면적><지번>65-2</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    23,000</거래금액><건축년도>2017</건축년도><년>2019</년><도로명>대학로</도로명><도로명건물본번호코드>00033</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>00</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100002</도로명코드><법정동> 효제동</법정동><법정동본번코드>0065</법정동본번코드><법정동부번코드>0002</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>16200</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>포레스트힐시티</아파트><월>1</월><일>1~10</일><일련번호>11110-2440</일련번호><전용면적>20.3861</전용면적><지번>65-2</지번><지역코드>11110</지역코드><층>12</층></item><item><거래금액>    20,500</거래금액><건축년도>2017</건축년도><년>2019</년><도로명>대학로</도로명><도로명건물본번호코드>00033</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>00</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100002</도로명코드><법정동> 효제동</법정동><법정동본번코드>0065</법정동본번코드><법정동부번코드>0002</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>16200</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>포레스트힐시티</아파트><월>1</월><일>11~20</일><일련번호>11110-2440</일련번호><전용면적>16.672</전용면적><지번>65-2</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    38,300</거래금액><건축년도>2003</건축년도><년>2019</년><도로명>성균관로17길</도로명><도로명건물본번호코드>00022</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100171</도로명코드><법정동> 명륜1가</법정동><법정동본번코드>0002</법정동본번코드><법정동부번코드>0012</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17000</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>송림아마레스아파트</아파트><월>1</월><일>11~20</일><일련번호>11110-127</일련번호><전용면적>53.42</전용면적><지번>2-12</지번><지역코드>11110</지역코드><층>6</층></item><item><거래금액>    73,500</거래금액><건축년도>1995</건축년도><년>2019</년><도로명>창경궁로</도로명><도로명건물본번호코드>00265</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>07</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3005008</도로명코드><법정동> 명륜2가</법정동><법정동본번코드>0004</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17100</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>아남1</아파트><월>1</월><일>1~10</일><일련번호>11110-25</일련번호><전용면적>84.8</전용면적><지번>4</지번><지역코드>11110</지역코드><층>2</층></item><item><거래금액>    85,000</거래금액><건축년도>1995</건축년도><년>2019</년><도로명>창경궁로</도로명><도로명건물본번호코드>00265</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>07</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3005008</도로명코드><법정동> 명륜2가</법정동><법정동본번코드>0004</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17100</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>아남1</아파트><월>1</월><일>1~10</일><일련번호>11110-25</일련번호><전용면적>84.9</전용면적><지번>4</지번><지역코드>11110</지역코드><층>17</층></item><item><거래금액>    65,000</거래금액><건축년도>1999</건축년도><년>2019</년><도로명>혜화로3길</도로명><도로명건물본번호코드>00005</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>02</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100545</도로명코드><법정동> 명륜2가</법정동><법정동본번코드>0237</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17100</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>아남3</아파트><월>1</월><일>11~20</일><일련번호>11110-26</일련번호><전용면적>65.78</전용면적><지번>237</지번><지역코드>11110</지역코드><층>4</층></item><item><거래금액>    35,000</거래금액><건축년도>1999</건축년도><년>2019</년><도로명>명륜4길</도로명><도로명건물본번호코드>00008</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100082</도로명코드><법정동> 명륜3가</법정동><법정동본번코드>0001</법정동본번코드><법정동부번코드>0030</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17300</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>한빛</아파트><월>1</월><일>11~20</일><일련번호>11110-27</일련번호><전용면적>59.73</전용면적><지번>1-30</지번><지역코드>11110</지역코드><층>3</층></item><item><거래금액>    29,000</거래금액><건축년도>1966</건축년도><년>2019</년><도로명>지봉로</도로명><도로명건물본번호코드>00025</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3005007</도로명코드><법정동> 창신동</법정동><법정동본번코드>0328</법정동본번코드><법정동부번코드>0017</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17400</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>동대문</아파트><월>1</월><일>11~20</일><일련번호>11110-30</일련번호><전용면적>28.8</전용면적><지번>328-17</지번><지역코드>11110</지역코드><층>3</층></item><item><거래금액>    29,000</거래금액><건축년도>1966</건축년도><년>2019</년><도로명>지봉로</도로명><도로명건물본번호코드>00025</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3005007</도로명코드><법정동> 창신동</법정동><법정동본번코드>0328</법정동본번코드><법정동부번코드>0017</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17400</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>동대문</아파트><월>1</월><일>11~20</일><일련번호>11110-30</일련번호><전용면적>28.8</전용면적><지번>328-17</지번><지역코드>11110</지역코드><층>3</층></item><item><거래금액>    13,000</거래금액><건축년도>2012</건축년도><년>2019</년><도로명>종로58가길</도로명><도로명건물본번호코드>00027</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100358</도로명코드><법정동> 숭인동</법정동><법정동본번코드>0296</법정동본번코드><법정동부번코드>0019</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>삼전솔하임2차</아파트><월>1</월><일>1~10</일><일련번호>11110-2322</일련번호><전용면적>14.69</전용면적><지번>296-19</지번><지역코드>11110</지역코드><층>9</층></item><item><거래금액>    13,500</거래금액><건축년도>2012</건축년도><년>2019</년><도로명>종로58가길</도로명><도로명건물본번호코드>00027</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100358</도로명코드><법정동> 숭인동</법정동><법정동본번코드>0296</법정동본번코드><법정동부번코드>0019</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>삼전솔하임2차</아파트><월>1</월><일>1~10</일><일련번호>11110-2322</일련번호><전용면적>16.67</전용면적><지번>296-19</지번><지역코드>11110</지역코드><층>5</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,000</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>14.48</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,000</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.42</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,000</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.42</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,000</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>14.48</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    11,300</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00017</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1392</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>주건축물제1동</아파트><월>1</월><일>11~20</일><일련번호>11110-2348</일련번호><전용면적>15.76</전용면적><지번>1392</지번><지역코드>11110</지역코드><층>10</층></item><item><거래금액>    12,500</거래금액><건축년도>2012</건축년도><년>2019</년><도로명>종로58가길</도로명><도로명건물본번호코드>00027</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100358</도로명코드><법정동> 숭인동</법정동><법정동본번코드>0296</법정동본번코드><법정동부번코드>0019</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>삼전솔하임2차</아파트><월>1</월><일>11~20</일><일련번호>11110-2322</일련번호><전용면적>14.69</전용면적><지번>296-19</지번><지역코드>11110</지역코드><층>5</층></item><item><거래금액>    11,300</거래금액><건축년도>2014</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00020</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1421</법정동본번코드><법정동부번코드>0002</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>숭인한양LEEPS</아파트><월>1</월><일>11~20</일><일련번호>11110-2366</일련번호><전용면적>12.78</전용면적><지번>1421-2</지번><지역코드>11110</지역코드><층>4</층></item><item><거래금액>    12,000</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00024</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1421</법정동본번코드><법정동부번코드>0001</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>종로동광모닝스카이</아파트><월>1</월><일>21~31</일><일련번호>11110-2343</일련번호><전용면적>15.855</전용면적><지번>1421-1</지번><지역코드>11110</지역코드><층>13</층></item><item><거래금액>    12,200</거래금액><건축년도>2013</건축년도><년>2019</년><도로명>난계로29가길</도로명><도로명건물본번호코드>00024</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100029</도로명코드><법정동> 숭인동</법정동><법정동본번코드>1421</법정동본번코드><법정동부번코드>0001</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>17500</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>종로동광모닝스카이</아파트><월>1</월><일>21~31</일><일련번호>11110-2343</일련번호><전용면적>15.855</전용면적><지번>1421-1</지번><지역코드>11110</지역코드><층>14</층></item><item><거래금액>    85,000</거래금액><건축년도>2004</건축년도><년>2019</년><도로명>평창12길</도로명><도로명건물본번호코드>00014</도로명건물본번호코드><도로명건물부번호코드>00004</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>4100488</도로명코드><법정동> 평창동</법정동><법정동본번코드>0179</법정동본번코드><법정동부번코드>0005</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>18300</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>에지앙빌</아파트><월>1</월><일>11~20</일><일련번호>11110-2292</일련번호><전용면적>110.61</전용면적><지번>179-5</지번><지역코드>11110</지역코드><층>2</층></item><item><거래금액>    57,500</거래금액><건축년도>2001</건축년도><년>2019</년><도로명>평창문화로</도로명><도로명건물본번호코드>00140</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100023</도로명코드><법정동> 평창동</법정동><법정동본번코드>0072</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>18300</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>롯데낙천대</아파트><월>1</월><일>21~31</일><일련번호>11110-71</일련번호><전용면적>84.21</전용면적><지번>72</지번><지역코드>11110</지역코드><층>5</층></item><item><거래금액>    35,500</거래금액><건축년도>1998</건축년도><년>2019</년><도로명>평창문화로</도로명><도로명건물본번호코드>00171</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100023</도로명코드><법정동> 평창동</법정동><법정동본번코드>0596</법정동본번코드><법정동부번코드>0001</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>18300</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>삼성</아파트><월>1</월><일>21~31</일><일련번호>11110-73</일련번호><전용면적>59.97</전용면적><지번>596</지번><지역코드>11110</지역코드><층>11</층></item><item><거래금액>    38,500</거래금액><건축년도>1998</건축년도><년>2019</년><도로명>평창문화로</도로명><도로명건물본번호코드>00171</도로명건물본번호코드><도로명건물부번호코드>00000</도로명건물부번호코드><도로명시군구코드>11110</도로명시군구코드><도로명일련번호코드>01</도로명일련번호코드><도로명지상지하코드>0</도로명지상지하코드><도로명코드>3100023</도로명코드><법정동> 평창동</법정동><법정동본번코드>0596</법정동본번코드><법정동부번코드>0000</법정동부번코드><법정동시군구코드>11110</법정동시군구코드><법정동읍면동코드>18300</법정동읍면동코드><법정동지번코드>1</법정동지번코드><아파트>삼성</아파트><월>1</월><일>21~31</일><일련번호>11110-73</일련번호><전용면적>59.97</전용면적><지번>596</지번><지역코드>11110</지역코드><층>8</층></item></items><numOfRows>1000</numOfRows><pageNo>1</pageNo><totalCount>35</totalCount></body></response>'
    #root = ET.fromstring(res.text)
    root = ET.fromstring(test)

    print(root)

    ## trade_price ## <거래금액> 82,500</거래금액>
    ## build_year ## <건축년도>2008</건축년도>
    ## trade_year ## <년>2015</년>
    # <도로명>사직로8길</도로명>
    # <도로명건물본번호코드>00004</도로명건물본번호코드>
    # <도로명건물부번호코드>00000</도로명건물부번호코드>
    # <도로명시군구코드>11110</도로명시군구코드>
    # <도로명일련번호코드>03</도로명일련번호코드>
    # <도로명지상지하코드>0</도로명지상지하코드>
    # <도로명코드>4100135</도로명코드>
    # <법정동> 사직동</법정동>
    # <법정동본번코드>0009</법정동본번코드>
    # <법정동부번코드>0000</법정동부번코드>
    # <법정동시군구코드>11110</법정동시군구코드>
    # <법정동읍면동코드>11500</법정동읍면동코드>
    # <법정동지번코드>1</법정동지번코드>
    ## apt_name ## <아파트>광화문풍림스페이스본(101동~105동)</아파트>
    ## trade_month ## <월>12</월>
    ## trade_days## <일>1~10</일>
    # <일련번호>11110-2203</일련번호>
    ## private_area ## <전용면적>94.51</전용면적>
    # <지번>9</지번>
    ## region_code ## <지역코드>11110</지역코드>
    ## floor ## <층>11</층>

    for item in root.findall('body/items/item'):
        #print(item[0].text)
        trade_price = float(item.find('거래금액').text.replace(',', '').strip())
        private_area = float(item.find('전용면적').text)
        unit_price =  trade_price / private_area
        print(trade_price, private_area, unit_price)



if __name__ == '__main__':
    init_db()
    print(json.dumps(test_analysis(),indent=4, sort_keys=True))

    # print ('------------------------test-------------------------')
    #

