# -*- coding: utf-8 -*-
from flask import request, render_template, jsonify, send_from_directory
from flask import Flask, url_for, redirect, session
import os, json, datetime
from module.database import db_session, init_db
from module.models import Position
from analysis import position_analysis
from utilities import gen_key, invalid_request
from flask_cors import CORS

app = Flask(__name__, static_folder='dist/static', template_folder='dist')

app.secret_key = 'sample_secreat_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

# enable CORS
CORS(app)

init_db()

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/test')
def test_db():
    db_session.add(Position('name','city','addr'))
    return 'success'


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

    position_items = request_json['position_list']

    # position_items = [
    #     {
    #         'name': '수정동1',
    #         'address': '경기도 어쩌구',
    #         'location_x': 10.222,
    #         'location_y': 25.241,
    #         'book_value' : 1000,
    #         'book_date': '2018-10-11',
    #         'position_type' : 'owner_occupied',
    #         'loan' : {
    #           'notional' : 10000,
    #           'loan_type': 0.012,
    #           'loan_rate' : 0.012,
    #           'maturity' : 2020-10-11
    #       },
    #         'rent': {
    #           'deposit': {
    #               'amount': 10000,
    #           },
    #           'payment': {
    #               'frequency': 'monthly',
    #               'amount': 1000
    #           },
    #           'start_date' : '2020-10-11',
    #           'maturity_date': '2020-10-11'
    #       },
    #     },
    #     {
    #         'name': '수정동2',
    #         'address': '경기도 어쩌구',
    #         'location_x': 10.222,
    #         'location_y': 25.241,
    #         'book_value' : 1000,
    #         'book_date': '2018-10-11',
    #         'position_type' : 'owner_occupied',
    #         'loan' : {
    #           'notional' : 10000,
    #           'loan_type': 0.012,
    #           'loan_rate' : 0.012,
    #           'maturity' : 2020-10-11
    #       },
    #         'rent': {
    #           'deposit': {
    #               'amount': 10000,
    #           },
    #           'payment': {
    #               'frequency': 'monthly',
    #               'amount': 1000
    #           },
    #           'start_date' : '2020-10-11',
    #           'maturity_date': '2020-10-11'
    #       },
    #     },
    # ]

    res = position_analysis(position_items)

    return jsonify(res)


@app.route('/storepositions', methods=['POST'])
def store_positions():
    # post
    request_json = request.json

    email = request_json['email']
    position_list = request_json['position_list']

    key = gen_key(email, position_list)
    #p = Position(key, email, positions)

    timestamp = str(datetime.datetime.utcnow())

    p = Position.query.filter(Position.email == email).first()

    if p is None:
        p = Position(key, email, json.dumps(position_list), timestamp)
        db_session.add(p)
    else:
        p.positions = json.dumps(position_list)
        p.key = key

    db_session.commit()

    res = dict()
    # res['access_key'] = key

    res['timestamp'] = timestamp
    res['message'] = 'success'
    res['access_key'] = key

    # email 보냄

    return jsonify(res)


@app.route('/getpositions', methods=['POST'])
def get_positions():
    # post
    request_json = request.json

    key = request_json['key']
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
        data['results'] = p.results

        res['data'] = data

    # email 보냄

    return jsonify(res)


@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/sitemap.xml')
def sitemap_to_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/google45f2d19c6c554811.html')
def google_site_confirm():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/naverac258554f02766a1a31c7f19cf6c4ae2.html')
def naver_site_confirm():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/downloads/<path:filename>', methods=['GET'])
def downlaod_file(filename):
    download_path = os.path.join('./downloads')
    return send_from_directory(download_path, filename=filename)


if __name__ == '__main__':
   app.run(debug = True)