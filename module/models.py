from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime
from module.database import Base, db_session
import datetime

class Position(Base):
    __tablename__ = 'positions'
    key = Column(String(128), primary_key=True)
    email = Column(String(120), unique=True)
    positions = Column(Text)
    results = Column(Text)
    timestamp = Column(String(30))

    def __repr__(self):
        return '<Position %r>' % (self.email)

    def __init__(self, key, email, positions, timestamp):
        self.key = key
        self.email = email
        self.positions = positions
        self.results = None
        self.timestamp = timestamp


def db_data_initialize():
    pass

