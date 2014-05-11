#-*- coding: utf-8 -*- 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR
from sqlalchemy import Boolean, Unicode
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash
from sqlalchemy import exc


engine = create_engine('sqlite:///works.db',
                       echo=True)
conn = engine.connect()

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Demount(Base):
    __tablename__ = 'DEMOUNT'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    dimension = Column(String)
    
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


try:
    Base.metadata.create_all(engine)
    print('connected')
except exc.OperationalError as e:
    print('e')
