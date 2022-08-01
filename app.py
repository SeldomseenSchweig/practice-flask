from crypt import methods
from unicodedata import name
from flask import Flask, redirect, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension
from models import Employee,EmployeeProject, Department, db, connect_db, get_directory, get_directory_join, get_directory_join_class, get_directory_all_join
from forms import EmployeeForm, AddSnackForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


toolbar = DebugToolbarExtension(app)
connect_db(app)

@app.route('/')
def home_age():
    return render_template('home.html')

@app.route('/phones')
def list_phones():
    emps = Employee.query.all()
    return render_template('phones.html',emps= emps)



@app.route('/employees/new', methods=["POST", "GET"])
def add_employee():
    """Adds Employees"""
    form = EmployeeForm()
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    if form.validate_on_submit():
        name=form.name.data
        state = form.state.data
        dept_code=form.dept_code.data
        
        new_employee= Employee(name=name, state =state, dept_code=dept_code)
        db.session.add(new_employee)
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('add_employee_form.html', form=form)



@app.route('/employees/<int:id>/edit', methods=["GET", "POST"])
def edit_employee(id):
    emp = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=emp)
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    if form.validate_on_submit():
        emp.name= form.name.data
        emp.state=form.state.data
        emp.dept_code.data = form.dept_code.data
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('edit_employee_form.html', form=form)











# ___________----------------------------------------------------

@app.route('/snacks/new', methods=["POST", "GET"])
def add_snack():
    form = AddSnackForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        raise
        flash(f"Created {name} -------${price}")
        return redirect('/')
    else:
        return render_template('add_snack_form.html', form = form)


