from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime, Float
from module.database import Base, db_session
import datetime

class UserLogin(Base):
    __tablename__ = 'userlogin'
    login_hash = Column(String(128), primary_key=True)
    access_token = Column(String(128))
    provider = Column(String(30))
    timestamp = Column(String(30))

    def __repr__(self):
        return '<Position %r>' % (self.email)

    def __init__(self, login_hash, access_token, provider, timestamp):
        self.login_hash = login_hash
        self.access_token = access_token
        self.provider = provider
        self.timestamp = timestamp


class Position(Base):
    __tablename__ = 'positions'
    key = Column(String(128), primary_key=True)
    email = Column(String(120))
    positions = Column(Text)
    results = Column(Text)
    timestamp = Column(String(30))

    def __repr__(self):
        return '<Position %r>' % (self.email)

    def __init__(self, key, email, positions, timestamp):
        self.key = key
        self.email = email
        self.positions = positions
        self.results = ''
        self.timestamp = timestamp


class Report(Base):
    __tablename__ = 'reports'
    key = Column(String(128), primary_key=True)
    position_token = Column(String(128))
    results = Column(Text)
    timestamp = Column(String(30))

    def __repr__(self):
        return '<Report %r>' % (self.email)

    def __init__(self, key, position_token, results, timestamp):
        self.key = key
        self.position_token = position_token
        self.results = results
        self.timestamp = timestamp


class TradePrice(Base):
    __tablename__ = 'tradeprices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tradeprice = Column(Float)
    yyyymm = Column(String(30))
    timestamp = Column(String(30))

    def __repr__(self):
        return '<Report %r>' % (self.email)

    def __init__(self, yyyymm, tradeprice, timestamp):
        self.yyyymm = yyyymm
        self.tradeprice = tradeprice
        self.timestamp = timestamp

def db_data_initialize():
    pass

