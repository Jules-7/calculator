from flask import render_template, request, redirect, url_for, flash
from flask import session
from database import db_session
from calculator import app
from forms import DemountForm, FloortForm, WallForm
from forms import DoorwayForm, CeilingForm, TileForm
from forms import ElectricForm, SanitaryForm, OtherForm

selected_data = {}

def make_record(db, works):
    if db in selected_data:
        for work in works:
            if work in selected_data[db]:
                pass
            else:
                selected_data[db].append(work)
    else:
        selected_data[db] = works

@app.route('/home', methods=['GET', 'POST'])
def show_work():
    demount = DemountForm(request.form)
    floor = FloortForm(request.form)
    wall = WallForm(request.form)
    doorway = DoorwayForm(request.form)
    ceiling = CeilingForm(request.form)
    tile = TileForm(request.form)
    electric = ElectricForm(request.form)
    sanitary = SanitaryForm(request.form)
    other = OtherForm(request.form)
    return render_template('home.html', demount=demount, floor=floor, 
                            wall=wall, doorway=doorway, ceiling=ceiling,
                            tile=tile, electric=electric, sanitary=sanitary,
                            other=other, selected_data=selected_data) 

@app.route('/home/<path:url>', methods=['GET', 'POST'])
def select_work(url):
    db = url
    form = DemountForm(request.form)
    if db:
        work = form.name.data
        make_record(str(db), work)
        #selected_data.append([str(db), selected])
    return redirect(url_for('show_work'))
