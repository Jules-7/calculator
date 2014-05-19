from wtforms import Form, TextField, validators, IntegerField
from wtforms import SelectMultipleField, widgets, PasswordField
import methods

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.TableWidget()
    option_widget = widgets.CheckboxInput()

class MultiTextField(SelectMultipleField):
    widget = widgets.TableWidget()
    option_widget = widgets.TextInput()

class DemountForm(Form):
    choices = methods.demount_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)


class FloorForm(Form):
    choices = methods.floor_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class WallForm(Form):
    choices = methods.wall_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class DoorwayForm(Form):
    choices = methods.doorway_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class CeilingForm(Form):
    choices = methods.ceiling_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class TileForm(Form):
    choices = methods.tile_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class ElectricForm(Form):
    choices = methods.electric_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class SanitaryForm(Form):
    choices = methods.sanitary_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class OtherForm(Form):
    choices = methods.other_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

'''
class SelectedForm(Form):
    name = MultiTextField()
'''
'''
class SelectedForm(Form):
    name = TextField()
    value = TextField()
'''
'''
class SelectedForm(Form):
    choices = methods.selected()
    value = MultiTextField('value',choices = choices)
'''

class AddRecordForm(Form):
    name = TextField("Name", [validators.Length(min=2, max=25)])
    work = TextField("Work type", [validators.Length(min=2, max=25)])
    price = TextField("Price", [validators.Length(min=2, max=25)])
    dimension = TextField("Dimension", [validators.Length(min=2, max=25)])


class EditForm(Form):
    id = TextField()
    name = TextField("name", [validators.Required()])
    price = TextField("price", [validators.Required()])
    dimension = TextField("dimension", [validators.Required()])


class RegisterForm(Form):
    username = TextField("User name", [validators.Required()])
    password = PasswordField("Password", [validators.Required()])


class LoginForm(Form):
    username = TextField("User name", [validators.Required()])
    password = PasswordField("Password", [validators.Required()])

class RateForm(Form):
    rate = TextField("rate", [validators.Required()])