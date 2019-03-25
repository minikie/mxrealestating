# -*- coding: utf-8 -*-
import requests
import hashlib
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import namedtuple
from bs4 import BeautifulSoup
from slimit.ast import String as astString
from slimit.parser import Parser
from slimit.visitors.nodevisitor import ASTVisitor
from urllib.parse import urlparse, parse_qsl


CF_Row = namedtuple('CF_Row', 'DATE IN OUT NET')


class NaverDataVisitor(ASTVisitor):
    def visit_Object(self, node):
        self.res = dict()

        for prop in node:
            left, right = prop.left, prop.right
            if type(right) is astString:
                self.res[left.value] = right.value
                # print('Property key=%s, value=%s' % (left.value, right.value))
            # visit all children in turn
            self.visit(prop)


def gen_key(email, positions):
    # print str(positions)
    _str = email + str(positions)

    return hashlib.sha256(_str.encode('utf-8')).hexdigest()


def get_hash(*args):
    # print str(positions)
    _str = ''
    for arg in args:
        _str += arg
    return hashlib.sha256(_str.encode('utf-8')).hexdigest()


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


def get_userinfo(user):
    if user.provider_type == 'naver':
        return user_info_from_naver(user)
    elif user.provider_type == 'daum':
        return user_info_from_daum(user)
    else:
        return None


def user_info_from_daum(user):
    pass


def user_info_from_naver(user):
    pass


def position_info_from_naver(url):
    parsed_obj = urlparse(url)
    article_info_no = 1
    if parsed_obj.netloc == 'm.land.naver.com':
        article_info_no = parsed_obj.path.split('/')[-1]
    elif parsed_obj.netloc == 'new.land.naver.com':
        article_info_no = dict(parse_qsl(parsed_obj.query))['articleNo']
    else:
        raise Exception('unknown url : ' + parsed_obj.netloc )

    r = requests.get('https://m.land.naver.com/article/info/' + str(article_info_no))
    soup = BeautifulSoup(r.content, "html.parser")
    res = dict()

    for sc in soup.findAll("script"):
        pos = sc.text.find('land.articleDetail.jsonPageData')
        if pos > 0:
            bracket_start_pos = sc.text.find('{',pos)
            bracket_end_pos = sc.text.find(';', pos)
            #print(sc.text[bracket_start_pos:bracket_end_pos])
            #js_obj_txt = sc.text[bracket_start_pos:bracket_end_pos]
            js_obj_txt = sc.text[pos:bracket_end_pos]
            # print(js_obj_txt)
            parser = Parser()
            tree = parser.parse(js_obj_txt)
            visitor = NaverDataVisitor()
            visitor.visit(tree)
            res = visitor.res

    return res


# hscpNo : '1347',
# 							ptpNo : '5',
# 							bildNo : '225825',
# 							priceStatsCount : '',
# 							lat:'37.562479',
# 							lng:'126.859997',
# 							tradTpCd : 'A1',
# 							tradTpNm : '매매',
# 							rletTpCd : 'APT',
# 							rletTpNm : '아파트',
# 							atclNo : '1906730376',
# 							atclNm : '가양6단지 613동',
# 							cortarNo : '1150010400',
# 							cortarNm : '서울시 강서구 가양동',
# 							dealAmt : '60000',
# 							wrntAmt : '0',
# 							rentAmt : '0',
# 							addr : '서울시 강서구 가양동 1485',
# 							spc : '75.89',
# 							dongNm : '613',
# 							prc : '60,000',
# 							prcBillion : '6억',
# 							notfSeq : '',
# 							isFavoriteItem : 'false',
# 							rltrId : 'leeck5areum',
# 							rltrTelNo : '02-3663-5333',
# 							rltrCphNo : '010-6617-9927',
# 							addr : '서울시 강서구 가양동 1485',
# 							isFromNaver : 'N',
# 							groundPlanImage : $.parseJSON('[{}]'),
# 							rmNo : '804',
# 							mapLocaIndcYn : 'Y',
#                             prcBillionRangeInfo : '6억',
# 							bssPrcs : bssPrcs,
# 							realPriceRecentYmInfo : $.parseJSON('{"recentRealPriceYm":"201903","recentRealPriceYmFmt1":"2019.03","recentRealPriceYmFmt2":"2019년 03월"}'),
#                             realPricePtpInfo : $.parseJSON('{"49.5":"2","39.6":"1","58.65":"5"}'),
# 							realPricePtpNmListStrInfo : $.parseJSON('{"49.5":"64㎡의 실거래가","39.6":"51㎡의 실거래가","58.65":"74A㎡, 75B㎡, 77C㎡의 실거래가"}'),
# 							realPriceExistYn : 'Y',
# 							ptpInfo : $.parseJSON('{"1":{"ptpNo":"1","ptpNm":"51","splySpc":"51.96","exclsSpc":"39.6","splySpcPyeong0WithUnit":"15평","splySpcPyeong2WithUnit":"15.71평","exclsSpcPyeong2WithUnit":"12평","exclsRate":"76","ptybyTotHsehCnt":"432","hscpTypeCd":"A01","ptpOrder":0,"ptpNmWithUnit":"51㎡","splySpcWithUnit":"51.96㎡","exclsSpcWithUnit":"39.6㎡"},"2":{"ptpNo":"2","ptpNm":"64","splySpc":"64.98","exclsSpc":"49.5","splySpcPyeong0WithUnit":"19평","splySpcPyeong2WithUnit":"19.65평","exclsSpcPyeong2WithUnit":"15평","exclsRate":"76","ptybyTotHsehCnt":"594","hscpTypeCd":"A01","ptpOrder":1,"ptpNmWithUnit":"64㎡","splySpcWithUnit":"64.98㎡","exclsSpcWithUnit":"49.5㎡"},"3":{"ptpNo":"3","ptpNm":"74A","splySpc":"74.58","exclsSpc":"58.65","splySpcPyeong0WithUnit":"22A평","splySpcPyeong2WithUnit":"22.56평","exclsSpcPyeong2WithUnit":"17.77평","exclsRate":"79","ptybyTotHsehCnt":"90","hscpTypeCd":"A01","ptpOrder":2,"ptpNmWithUnit":"74A㎡","splySpcWithUnit":"74.58㎡","exclsSpcWithUnit":"58.65㎡"},"4":{"ptpNo":"4","ptpNm":"77C","splySpc":"77.37","exclsSpc":"58.65","splySpcPyeong0WithUnit":"23C평","splySpcPyeong2WithUnit":"23.4평","exclsSpcPyeong2WithUnit":"17.77평","exclsRate":"76","ptybyTotHsehCnt":"120","hscpTypeCd":"A01","ptpOrder":4,"ptpNmWithUnit":"77C㎡","splySpcWithUnit":"77.37㎡","exclsSpcWithUnit":"58.65㎡"},"5":{"ptpNo":"5","ptpNm":"75B","splySpc":"75.89","exclsSpc":"58.65","splySpcPyeong0WithUnit":"22B평","splySpcPyeong2WithUnit":"22.95평","exclsSpcPyeong2WithUnit":"17.77평","exclsRate":"77","ptybyTotHsehCnt":"240","hscpTypeCd":"A01","ptpOrder":3,"ptpNmWithUnit":"75B㎡","splySpcWithUnit":"75.89㎡","exclsSpcWithUnit":"58.65㎡"}}'),
# 							zoom : '11',
# 							prcCpId : 'kbstar'

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


def test1():
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

    # print (df1.append(df2)).groupby('DATE').sum().to_json(orient='split')
    df = (df1.append(df2)).groupby('DATE').sum()
    # print df.to_json(orient='split')
    # print df.to_json(orient='index')
    # print df.to_json(orient='records')
    # print df.to_json(orient='columns')
    # from flask import jsonify

    # print df['IN']

    # import numpy as np
    # take_smaller = lambda s1, s2: s1+s2
    # print df1.combine(df2, take_smaller)

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
    # print(position_info_from_naver('https://m.land.naver.com/article/info/1905842490'))
    # http://www.juso.go.kr/addrlink/addressBuildDevNew.do?menu=rdnm
    pass


