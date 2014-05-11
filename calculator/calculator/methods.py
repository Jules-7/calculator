#-*-coding: utf-8-*-
from database import db_session, Demount, Floor, Wall, Doorway
from database import Ceiling, Tile, Electric, Sanitary, Other
from sqlalchemy import *

def demount_works():
    names = db_session.query(Demount.id, Demount.name).all()
    return names

def floor_works():
    names = db_session.query(Floor.id, Floor.name).all()
    return names

def wall_works():
    names = db_session.query(Wall.id, Wall.name).all()
    return names

def doorway_works():
    names = db_session.query(Doorway.id, Doorway.name).all()
    return names

def ceiling_works():
    names = db_session.query(Ceiling.id, Ceiling.name).all()
    return names

def tile_works():
    names = db_session.query(Tile.id, Tile.name).all()
    return names

def electric_works():
    names = db_session.query(Electric.id, Electric.name).all()
    return names

def sanitary_works():
    names = db_session.query(Sanitary.id, Sanitary.name).all()
    return names

def other_works():
    names = db_session.query(Other.id, Other.name).all()
    return names



#demount_works()