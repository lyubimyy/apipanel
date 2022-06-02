import datetime
import sqlalchemy as _sql
import database as db
from sqlalchemy import Column, Integer, String, DateTime, TEXT, ForeignKey


class Domain(db.Model):
    __tablename__ = 'domain'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    domain = Column('domain', String)


class Event(db.Model):
    __tablename__ = 'event'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    event = Column('event', Integer)
    time_add = Column('time_add', DateTime, default=datetime.datetime.utcnow)
    domain_id = Column(Integer, ForeignKey("domain.id"))


class Version(db.Model):
    __tablename__ = 'version'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    version = Column('version', Integer)
    domain_id = Column(Integer, ForeignKey("domain.id"))


class Message(db.Model):
    __tablename__ = 'message'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    message = Column('message', TEXT, default=None)
    domain_id = Column(Integer, ForeignKey("domain.id"))