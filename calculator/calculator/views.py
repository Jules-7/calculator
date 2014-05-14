from flask import render_template, request, redirect, url_for, flash
from flask import session, jsonify
import json
from database import db_session, Work
from calculator import app
from forms import DemountForm, TileForm
from forms import LoginForm, RegisterForm
import methods
from sqlalchemy.exc import IntegrityError
from forms import WallForm, FloorForm
from forms import DoorwayForm, CeilingForm
from forms import ElectricForm, SanitaryForm, OtherForm



def make_record(works):
    if session['data']:
        if not works:
            pass
        else:
            for work in works:
                session['data'].append(work)


@app.route('/home', methods=['GET', 'POST'])
def show_work():
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
    for each in session['data']:
        chosen.append(each)
    flash('%s'%session['data'])
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


@app.route('/add_numbers')
def add_numbers():
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
            session['present'] = 'present'
            session["logout"] = False
            return redirect(url_for('show_work'))
        elif session["permission"] == "authorized":
            session['data'] = [0]
            session['present'] = 'present'
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