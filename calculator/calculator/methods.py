#-*-coding: utf-8-*-
from database import db_session, Work, User
from werkzeug.security import check_password_hash
from flask import session

def demount_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Демонтаж").all()
    return names

def floor_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Пол").all()
    return names

def wall_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Стены").all()
    return names

def doorway_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Проемы").all()
    return names

def ceiling_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Потолок").all()
    return names

def tile_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Плитка").all()
    return names

def electric_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Электрика").all()
    return names

def sanitary_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Сантехника").all()
    return names

def other_works():
    names = db_session.query(Work.id, Work.name).filter(Work.work==u"Разное").all()
    return names

def get_all_ids():
    ids = db_session.query(Work.id).distinct().all()
    all_ids = [each[0] for each in ids]
    return all_ids

def get_selected(ids):
    #choices = []
    #for each in ids:
        #if isinstance(each, list):
            #for inner_each in each:
                #choices.append(inner_each)
        #else:
            #choices.append(each)
    selected = {}
    for each in ids:
        if each == 0:
            pass
        else:
            data = db_session.query(Work.name, Work.dimension, Work.work).filter(Work.id==each).all()
            data = data[0]
            data = [dat for dat in data]
            if data[2] in selected:
                selected[data[2]].append([data[0], each, data[1]])
            else:
                selected[data[2]] = [[data[0], each, data[1]]]
            #selected[each] = data
    return selected

#print(get_selected([1,5,8]))

def calc(ids, amount):
    prices = db_session.query(Work.price).filter(Work.id.in_((ids))).all()
    prices = [each[0] for each in prices] 
    i = 0
    result = 0
    while i < len(ids):
        result += prices[i]*amount[i]
        i += 1
    return result

#print(calc([1,2,3,4,5,6], [3,3,3,3,3,3]))

def add_user(username, password, is_admin = False):
    new_user = User(username, password, is_admin)
    db_session.add(new_user)
    db_session.commit()

def db_test_admin():
    admin_present = db_session.query(User).filter_by(username = 'admin').first()
    if admin_present:
        pass
    else:
        add_user('admin', '123', is_admin=True)

""" create admin record in db"""
db_test_admin()

def check_if_admin(username, password):
    find_password = db_session.query(User.password).filter(User.username == username).first()
    if find_password:
        find_password = find_password[0]
        check = check_password_hash(find_password, password)
        if check:
            session["username"] = username
            is_authorized = db_session.query(User.is_admin).filter(User.username == username).first()
            is_authorized = is_authorized[0]
            if is_authorized:
                session["permission"] = "authenticated"
            else:
                session["permission"] = "authorized"
        else:
            session["permission"] = "incorrect"
    else:
        session["permission"] = "denied"




#demount_works()