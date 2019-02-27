# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from sqlalchemy import create_engine, Integer, Column, String, Text, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import models
from analysis import position_analysis
from utilities import gen_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
engine = create_engine('sqlite:///students.sqlite3', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Position(Base):
    __tablename__ = 'users'
    key = Column(String(50), primary_key=True)
    email = Column(String(50))
    positions = Column(Text)
    results = Column(Text)

    def __init__(self, key, email, positions):
        self.key = key
        self.email = email
        self.positions = positions
        self.results = None


@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'


@app.route('/test')
def test_db():
    Session.add(Position('name','city','addr'))
    return 'success'


# 예전에 저장했던 데이터
# private로 하면 검색안됨고 email필요한걸로 redirect
@app.route('/data/<keyname>')
def load_info(keyname):
    return keyname


# ajax call
@app.route('/analysis')
def analysis():
    post_data=dict()

    #position_items = post_data['position_items']
    position_items = [
        {
            'name': '수정동1',
            'address': '경기도 어쩌구',
            'location_x': 10.222,
            'location_y': 25.241,
            'book_value' : 1000,
            'book_date': '2018-10-11',
            'position_type' : 'owner_occupied',
            'loan' : {
              'notional' : 10000,
              'loan_type': 0.012,
              'loan_rate' : 0.012,
              'maturity' : 2020-10-11
          },
            'rent': {
              'deposit': {
                  'amount': 10000,
              },
              'payment': {
                  'frequency': 'monthly',
                  'amount': 1000
              },
              'start_date' : '2020-10-11',
              'maturity_date': '2020-10-11'
          },
        },
        {
            'name': '수정동2',
            'address': '경기도 어쩌구',
            'location_x': 10.222,
            'location_y': 25.241,
            'book_value' : 1000,
            'book_date': '2018-10-11',
            'position_type' : 'owner_occupied',
            'loan' : {
              'notional' : 10000,
              'loan_type': 0.012,
              'loan_rate' : 0.012,
              'maturity' : 2020-10-11
          },
            'rent': {
              'deposit': {
                  'amount': 10000,
              },
              'payment': {
                  'frequency': 'monthly',
                  'amount': 1000
              },
              'start_date' : '2020-10-11',
              'maturity_date': '2020-10-11'
          },
        },
    ]

    res = position_analysis(position_items)

    return jsonify(res)


@app.route('/storepositions')
def store_positions():
    # post
    post_data = dict()

    email = post_data['email']
    key = gen_key(email)
    positions = post_data['positions']
    p = Position(key, email, positions)

    exist = True

    if exist:
        db.session.delete(p)

    db.session.add(p)

    return key


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)