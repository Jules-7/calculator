from flask import render_template, request, redirect, url_for, flash
from flask import session, jsonify
from datetime import timedelta
from database import db_session
from calculator import app
from forms import DemountForm, TileForm
from forms import LoginForm, RegisterForm
import methods
from sqlalchemy.exc import IntegrityError
from forms import WallForm, FloorForm
from forms import DoorwayForm, CeilingForm
from forms import ElectricForm, SanitaryForm, OtherForm
from forms import AddRecordForm, EditForm, RateForm
#3from flask.ext.login import LoginManager
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_required, login_user, 
                         current_user, logout_user, UserMixin)
from database import User


login_manager = LoginManager()
'''The login manager contains the code that lets your application
 and Flask-Login work together, such as how to load a user from an ID, 
 where to send users when they need to log in, and the like.

Once the actual application object has been created,
 you can configure it for login with:'''

login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


def make_record(works):
    #try:
    #if session['data']:
        #if not works:
            #pass
        #else:
    for work in works:
        try:
            present = session['data']
            if work in present:
                pass
            else:
                session['data'].append(work)
        except:
            session['data'] = [0]


@app.route('/home', methods=['GET', 'POST'])
def show_work():
    
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30) 
    
    demount = DemountForm(request.form)
    floor = FloorForm(request.form)
    wall = WallForm(request.form)
    doorway = DoorwayForm(request.form)
    ceiling = CeilingForm(request.form)
    tile = TileForm(request.form)
    electric = ElectricForm(request.form)
    sanitary = SanitaryForm(request.form)
    other = OtherForm(request.form)
    chosen = []
    try:
        for each in session['data']:
            chosen.append(each)
    except:
        session['data'] = [0]
    #flash('%s'%session['data'])
    selected = methods.get_selected(chosen)
    return render_template('home.html', demount=demount, tile=tile, selected=selected,
                           floor=floor, wall=wall, doorway=doorway, ceiling=ceiling,
                           electric=electric, sanitary=sanitary, other=other)


@app.route('/home/<path:url>', methods=['GET', 'POST'])
def select_work(url):
    db = url
    if db:
        form = DemountForm(request.form)
        work = form.name.data
        make_record(work)
    return redirect(url_for('show_work'))


@app.route('/get_result')
def get_result():
    ident = []
    amount = []
    ids = methods.get_all_ids()
    for each in ids:
        value = request.args.get(str(each), '0', type=str)
        if int(value) != 0:
            ident.append(each)
            amount.append(int(value))
    res = methods.calc(ident, amount)
    return jsonify(result=res)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    try:
        if (request.method == 'POST') and form.validate():
            methods.add_user(form.username.data, form.password.data)
            flash('You are registered.')
            flash('You can login now.')
            login = True
            return render_template('register.html', form = form, login = login)
        elif request.method == 'POST':
            flash("Fill all fields, please")
    except IntegrityError:
        db_session.rollback()
        flash('That User name is not available')
        return render_template('register.html', form = form)
    return render_template('register.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if (request.method == 'POST') and form.validate():
        methods.check_if_admin(form.username.data, form.password.data)
        if session["permission"] == "authenticated":
            session['data'] = [0]
            #session['present'] = 'present'
            session["logout"] = False
            return redirect(url_for('show_work'))
        elif session["permission"] == "authorized":
            session['data'] = [0]
            #session['present'] = 'present'
            session["logout"] = False
            return redirect(url_for('show_work'))
        elif session["permission"] == "incorrect":
            flash('Wrong password. Try again.')
            register = True
            return render_template('login.html', form = form, register = register)
        elif session["permission"] == "denied":
            register = False
            flash('No such user. You need to register first')
            return render_template('login.html', form = form, register = register)
    elif request.method == 'POST' and form.username.data =='' or \
            form.password.data == '':
        flash('Fill in all fields, please.')
        return render_template('login.html', form = form)
    else:
        return render_template('login.html', form = form)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop("username")
    session.pop("permission")
    session["data"] = [0]
    return redirect(url_for('show_work'))


@app.route('/clear')
def clear_selection():
    session['data'] = [0]
    return redirect(url_for('show_work'))


@app.route('/delete/<path:url>')
def delete(url):
    chosen = []
    for each in session['data']:
        chosen.append(each)
    chosen.remove(int(url))
    session['data'] = chosen
    return redirect(url_for('show_work'))


@app.route('/database')
def show_database():
    add_form = AddRecordForm(request.form)
    database = methods.get_db()
    rate_form = RateForm(request.form)
    current_rate = methods.get_current_rate()
    return render_template('database.html', database = database, add_form = add_form, rate_form = rate_form, 
                           current_rate = current_rate)


@app.route('/deletefromdb/<path:url>')
def delete_record(url):
    methods.del_record(url)
    return redirect(url_for('show_database'))


@app.route('/add_record', methods = ['GET', 'POST'])
def add_record():
    add_form = AddRecordForm(request.form)
    if request.method == 'POST' and request.form['btn'] == 'add':
        flash('got post')
        methods.add_record(add_form.name.data, add_form.work.data, add_form.price.data, add_form.dimension.data)
    return redirect(url_for('show_database'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    e_form = EditForm(request.form)
    e_form.id = int(id)
    edit = True
    add_form = AddRecordForm(request.form)
    rate_form = RateForm(request.form)
    database = methods.get_db()
    return render_template('database.html', e_form=e_form, edit = edit, database = database, add_form = add_form,
                            rate_form = rate_form)


@app.route('/edit_name/<int:id>', methods=['GET', 'POST'])
def edit_record(id):
    e_form = EditForm(request.form)
    add_form = AddRecordForm(request.form)
    database = methods.get_db()
    if request.form['btn'] == 'edit':
        id = id
        name = e_form.name.data
        price = e_form.price.data
        dimension = e_form.dimension.data
        methods.edit(id, name, price, dimension)
        return redirect(url_for('show_database'))
    return redirect(url_for('show_database'))


@app.route('/change_rate', methods = ['GET', 'POST'])
def change_rate():
    rate_form = RateForm(request.form)
    if request.form['btn'] == "rate":
        rate = rate_form.rate.data
        methods.new_rate(rate)
        return redirect(url_for('show_database'))
    return redirect(url_for('show_database'))