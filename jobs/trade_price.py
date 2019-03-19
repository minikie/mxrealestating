from module.database import db_session, init_db
from module.models import TradePrice
from analysis import download_trade_price
import datetime


# https://financedata.github.io/posts/korea-area-code.html

def start():
    # 현재월
    today = datetime.datetime.today()
    # yyyymm = str(today.year) + str(today.month)
    yyyymm = today.strftime('%Y%m')
    region_codes = [11110, 11112]

    for rc in region_codes:
        download_trade_price(rc, yyyymm)


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
