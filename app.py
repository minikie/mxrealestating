# -*- coding: utf-8 -*-
from pandas import util

from flask import request, render_template, jsonify, send_from_directory
from flask import Flask, url_for, redirect, session, make_response, abort
import os, json, datetime
from module.database import db_session, init_db
from module.models import Position, UserLogin, Report
from analysis import position_analysis
import utilities, random
#from utilities import gen_key, invalid_request,

from flask_cors import CORS

app = Flask(__name__, static_folder='dist/static', template_folder='dist')

app.secret_key = 'sample_secreat_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

# enable CORS
CORS(app)

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    #resp = make_response(render_template('index.html'))
    # resp.set_cookie('position_token', utilities.get_hash(str(random.random()),str(random.random())))
    # return resp
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def index_test():
    # resp = make_response(render_template('index.html'))
    # resp.set_cookie('userID', 'testID')

    # ------------------------------------------------------------------------
    # Get 인 경우에
    # if cookie 가 없으면 redirect -> login.html
    # cookie 가 있으면 index.html 로 가는데 거기서 js 에서 쿠키로 user정보가져옴
    if request.method == 'GET':
        login_hash = request.cookies.get('login_hash')
        if login_hash is None:
            return redirect(url_for('login'))

        user = UserLogin.query.filter(UserLogin.login_hash == login_hash).first()

        if user is None:
            return redirect(url_for('login'))

        # naver에 서 받아와봄
        userinfo = utilities.get_userinfo(user)

        if userinfo is None:
            return redirect(url_for('login'))

        return render_template('index.html')

    # Post 인 경우에는
    # token이 날라올거기 때문에
    # 내부에 ip, token, hash 를 저장하고 hash를 쿠키에 담아서 날려줌
    # cookie 가 있으므로 index.html로 거기서 js 에서 쿠키로 user정보가져옴
    elif request.method == 'POST':
        access_token = request.json['token']
        ip = request.remote_addr
        login_hash = utilities.get_hash(access_token, ip)

        user = UserLogin.query.filter(UserLogin.access_token == access_token).first()
        timestamp = str(datetime.datetime.utcnow())
        provider = 'naver'

        if user is None:
            user = UserLogin(login_hash, access_token, provider, timestamp)
            db_session.add(user)
        else:
            user.access_token = access_token
            user.login_hash = login_hash
            user.provider = provider
            user.timestamp = timestamp

        db_session.commit()
    else:
        return redirect(url_for('login'))

    return render_template('index.html')


    #return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/cookie')
def cookie():
    name = request.cookies.get('myname')
    return '<h1>welcome ' + name + '</h1>'



@app.route('/test')
def test_index():
    return render_template('index.html')


# 예전에 저장했던 데이터
# private로 하면 검색안됨고 email필요한걸로 redirect
@app.route('/data/<keyname>')
def load_info(keyname):
    return keyname


# ajax call
@app.route('/analysis', methods=['POST'])
def analysis():
    # post
    request_json = request.json

    position_token = request_json['position_token']
    position_items = request_json['position_list']

    if len(position_items) == 0:
        abort(400, 'position_list is empty')

    res = position_analysis(position_items)
    res['results_data']['timestamp'] = str(datetime.datetime.utcnow())

    p = Position.query.filter(Position.key == position_token).first()

    if p is not None:
        p.results = json.dumps(res['results_data'])
        db_session.commit()

    return jsonify(res)


@app.route('/storepositions', methods=['POST'])
def store_positions():
    #position_token = request.cookies.get('position_token')

    # post
    request_json = request.json

    print(request_json)

    email = request_json['email']
    position_token = request_json['position_token']
    position_list = request_json['position_list']
    results_data = json.dumps(request_json['results_data'])

    #key = utilities.gen_key(email, position_list)
    #p = Position(key, email, positions)

    timestamp = str(datetime.datetime.utcnow())

    p = Position.query.filter(Position.key == position_token).first()

    if p is None:
        p = Position(position_token, email, json.dumps(position_list), timestamp)
        p.results = results_data
        db_session.add(p)
    else:
        p.positions = json.dumps(position_list)
        p.results = results_data
        p.key = position_token
        p.timestamp = timestamp


    db_session.commit()

    res = dict()
    # res['access_key'] = key

    res['timestamp'] = timestamp
    res['message'] = 'success'

    # email 보냄

    return jsonify(res)


@app.route('/getpositions', methods=['POST'])
def get_positions():
    # post
    request_json = request.json

    key = request_json['position_token']
    # p = Position(key, email, positions)

    p = Position.query.filter(Position.key == key).first()

    res = dict()
    # res['access_key'] = key
    timestamp = str(datetime.datetime.utcnow())
    res['timestamp'] = timestamp
    res['message'] = 'success'

    if p is None:
        res['message'] = 'fail'
        return jsonify(res)
    else:
        data = dict()
        data['userinfo'] = dict()
        data['userinfo']['email'] = p.email
        data['position_list'] = json.loads(p.positions)
        if p.results == '' or p.results is None:
            data['results_data'] = None
        else:
            data['results_data'] = json.loads(p.results)

        res['data'] = data

    # email 보냄

    return jsonify(res)


@app.route('/parse_position_info', methods=['POST'])
def parse_position_info():
    # post
    request_json = request.json

    url = request_json['url']
    position_info = utilities.position_info_from_naver(url)

    res = dict()
    timestamp = str(datetime.datetime.utcnow())

    # res['access_key'] = key

    # https://m.land.naver.com/article/info/1905842490
    # 화면
    print(position_info['addr'])
    print(position_info['atclNm'])

    res['address'] = str(position_info['addr'] + ' ' + position_info['atclNm']).replace("'","")
    res['apt_name'] = position_info['atclNm']
    res['legal_dong'] = position_info['cortarNm'] #
    res['private_area'] = position_info['spc'] # 면적
    res['currenct_price'] = position_info['dealAmt']  # 현재가격(만원)

    #내부용
    res['region_code'] = position_info['atclNo'] # 법정동 코드

    res['timestamp'] = timestamp
    res['message'] = 'success'

    # email 보냄

    return jsonify(res)


@app.route('/export_report', methods=['POST'])
def export_report():
    request_json = request.json

    report_token = request_json['report_token']
    position_token = request_json['position_token'] # report owner
    results_data = json.dumps(request_json['results_data'])

    r = Report.query.filter(Report.key == report_token and Report.position_token == position_token).first()
    timestamp = str(datetime.datetime.utcnow())

    if r is None:
        r = Report(report_token, position_token, results_data, timestamp)
        db_session.add(r)
    else:
        r.results = results_data
        r.timestamp = timestamp

    db_session.commit()

    res = dict()

    res['timestamp'] = timestamp
    res['message'] = 'success'

    return jsonify(res)


@app.route('/report/<report_token>', methods=['GET'])
def get_report(report_token):
    r = Report.query.filter(Report.key == report_token).first()

    # timestamp = str(datetime.datetime.utcnow())

    if r is None:
        abort(400, 'no report exist')
    else:
        report_data = json.loads(r.results)
        return render_template('report.html', report_data=report_data)


# --------------------------------------------------------------------------------------------------
# site setting ----------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/sitemap.xml')
def sitemap_to_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/google45f2d19c6c554811.html')
def google_site_confirm():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/naver_site_login_callback.html')
def naver_site_login_callback():
    # call back 처리
    # id 성별 등 랑 조회할수 있는 것들이 있음
    # token을 ip랑 hash 랑 맹글어서 저장함.

    return 'success'


@app.route('/naverac258554f02766a1a31c7f19cf6c4ae2.html')
def naver_site_confirm():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/downloads/<path:filename>', methods=['GET'])
def downlaod_file(filename):
    download_path = os.path.join('./downloads')
    return send_from_directory(download_path, filename=filename)


if __name__ == '__main__':
   app.run(debug = True)