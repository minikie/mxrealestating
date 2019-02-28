from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime
from database import Base, db_session
import datetime

class Position(Base):
    __tablename__ = 'positions'
    key = Column(String(128), primary_key=True)
    email = Column(String(120), unique=True)
    positions = Column(Text)
    results = Column(Text)

    def __repr__(self):
        return '<Position %r>' % (self.email)

    def __init__(self, key, email, positions):
        self.key = key
        self.email = email
        self.positions = positions
        self.results = None

    def get_dict(self):
        info = {}
        info['email'] = self.email
        info['license_key'] = self.license_key
        info['maturitydate'] = self.maturitydate
        info['ctoken'] = self.ctoken

        return info


def db_data_initialize():
    pass