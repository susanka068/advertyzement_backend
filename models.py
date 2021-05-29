from sqlalchemy import *
from sqlalchemy.log import echo_property
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True , echo = True )
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Banks(Base):
    __tablename__ = 'banks'
    name = Column(String)
    id = Column(Integer, primary_key=True)


class Branches(Base):
    __tablename__ = 'branches'
    ifsc = Column(String, primary_key = True )
    bank_id = Column(  Integer , ForeignKey('banks.id') )
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank = relationship(
        Banks,
        backref=backref('branches', uselist=True, cascade='delete,all'))