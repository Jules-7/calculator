from wtforms import Form, BooleanField, TextField, validators
from wtforms import SelectMultipleField, widgets
import methods

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.TableWidget()
    option_widget = widgets.CheckboxInput()

class DemountForm(Form):
    choices = methods.demount_works()
    name = MultiCheckboxField("Select", choices = choices, coerce=int)

class FloortForm(Form):
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