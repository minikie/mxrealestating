from module.database import db_session, init_db
from module.models import TradePrice
import pandas as pd
import requests
import datetime

api_key = 'open_api_key'
init_db()

# https://financedata.github.io/posts/korea-area-code.html

def start():
    # 현재월
    today = datetime.datetime.today()
    yyyymm = str(today.year) + str(today.month)
    parameters = { 'LAWD_CD': 'value1',
                   'DEAL_YMD': 'value2',
                   'numOfRows': 1000,
                   'serviceKey': api_key }

    #url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?_wadl&type=xml'

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?_wadl&type=xml'
    res = requests.get(url, params=parameters)

    # res -> xml parsing
    df = pd.DataFrame()

    timestamp = str(datetime.datetime.utcnow())

    # 지워지나..?
    TradePrice.query.filter(TradePrice.yyyymm == yyyymm).delete()

    for i in df:
        db_session.add(TradePrice(yyyymm, 0.0, timestamp))

    db_session.commit()


def test_data_insert():
    yyyymm = '201903'
    timestamp = str(datetime.datetime.utcnow())
    for i in range(1,10):
        db_session.add(TradePrice(yyyymm, i, timestamp))

    db_session.commit()


def test_data_delete():
    yyyymm = '201903'
    TradePrice.query.filter(TradePrice.yyyymm == yyyymm).delete()

    db_session.commit()


if __name__ == '__main__':
    test_data_insert()
    test_data_delete()
