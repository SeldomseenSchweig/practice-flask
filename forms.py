from unicodedata import category, name
from xmlrpc.client import boolean
from flask_wtf import FlaskForm
from wtforms import RadioField,IntegerField, StringField, FloatField, BooleanField, SelectField


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



class NewEmployeeForm(FlaskForm):
    name = StringField("Employee Name")
    state= StringField("State")
    dept_code = SelectField('Department Code')
        