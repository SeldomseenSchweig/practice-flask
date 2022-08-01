from unicodedata import category, name
from xmlrpc.client import boolean
from flask_wtf import FlaskForm
from wtforms import RadioField,IntegerField, StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired

class AddSnackForm(FlaskForm):
    """Adds snack to form"""
    name = StringField("Snack name")
    price = FloatField("Price of Snack in USD")
    is_healthy = BooleanField( "Healthy Snack?")
    quantity = IntegerField("How many?")
    # category = RadioField('Category', choices= [
    #     ('sweet','Candy'), ('spicy','Spicy/hot'), ('cold','ice cold')]

    #     )
    category = SelectField('Category', choices= [
        ('sweet','Candy'), ('spicy','Spicy/hot'), ('cold','ice cold')]
        )



class EmployeeForm(FlaskForm):
    name = StringField("Employee Name", validators=[InputRequired])
    state= StringField("State")
    dept_code = SelectField('Department Code')
        