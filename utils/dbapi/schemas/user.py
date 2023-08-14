from utils.dbapi.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float, INTEGER


class User(TimedBaseModel):
    __tablename__ = 'user'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    f_name = Column(String(200))
    l_name = Column(String(200))
    username = Column(String(50))
    referral_id = Column(BigInteger)
    status = Column(String(30))
    balance = Column(Float)
    card_day = Column(String(50))

    query: sql.select


class Card(TimedBaseModel):
    __tablename__ = 'card'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    card_name = Column(String(200))
    card_pic = Column(String(200))
    card_type = Column(String(200))
    card_info = Column(String(5000))
    card_zn = Column(String(5000))
    card_obzn = Column(String(5000))
    card_lock_you = Column(String(5000))
    card_data = Column(String(200))
    card_back = Column(String(5000))
    card_tyday = Column(String(5000))
    card_next = Column(String(5000))
    yes_no = Column(String(5000))
    card_cratc = Column(String(2000))
    card_cratc_obr = Column(String(2000))
    card_day = Column(String(2000))

    query: sql.select


class Check(TimedBaseModel):
    __tablename__ = 'check'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    bill_id = Column(String(255))
    user_id = Column(BigInteger)
    amount = Column(BigInteger)
    url_p = Column(String(500))

    query: sql.select


class Promocode(TimedBaseModel):
    __tablename__ = 'promo-code'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50), primary_key=True)
    amount = Column(BigInteger)

    query: sql.select


class Promoactive(TimedBaseModel):
    __tablename__ = 'promo-active'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50))
    user_id = Column(BigInteger)

    query: sql.select