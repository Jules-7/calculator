#-*- coding: utf-8 -*- 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Boolean
from werkzeug.security import generate_password_hash
from sqlalchemy import exc


engine = create_engine('sqlite:///works.db', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Work(Base):

    __tablename__ = 'WORK'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    work = Column(String)
    price = Column(Integer)
    dimension = Column(String)
    

class User(Base):
    
    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = self.set_password(password)
        self.is_admin = is_admin

    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean)

    def set_password(self, password):
        return generate_password_hash(password)


class DollarRate(Base):
    
    def __init__(self, rate):
        self.rate = rate
    
    __tablename__ = 'RATE'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rate = Column(Integer)

try:
    Base.metadata.create_all(engine)
except exc.OperationalError as e:
    print('e')



'''
class Floor(Base):
    __tablename__ = 'FLOOR'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)
    
class Wall(Base):
    __tablename__ = 'WALL'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Doorway(Base):
    __tablename__ = 'DOORWAY'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Ceiling(Base):
    __tablename__ = 'CEILING'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Tile(Base):
    __tablename__ = 'TILE'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Electric(Base):
    __tablename__ = 'ELECTRIC'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Sanitary(Base):
    __tablename__ = 'SANITARY'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)

class Other(Base):
    __tablename__ = 'OTHER'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)
'''