from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime
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


def db_data_initialize():
    pass

