"""Sample file demonstrating SQLAlchemy joins & relationships."""

from email.policy import default
from enum import unique
from flask_sqlalchemy import SQLAlchemy

# This is the connection to the database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# models below

class Employee(db.Model):
    """Employee model"""
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable = False, default='CA')
    dept_code = db.Column(db.Text, 
                db.ForeignKey('departments.dept_code'))

    department = db.relationship('Department', backref = 'employees')
    assignments = db.relationship('EmployeeProject', backref= 'employee')
    projects= db.relationship('Project', secondary='employees_projects', backref = 'employees')

    def __repr__(self):
        return f" {self.name}, department of {self.dept_code}, in {self.state} "


class Department(db.Model):
    """DEPARTMENT MODEL"""

    __tablename__ = 'departments'

    dept_code = db.Column(db.Text, primary_key = True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)
    def __repr__(self):
        return f"{self.dept_code}, department of {self.dept_name}, {self.phone} "


class Project(db.Model):

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text, primary_key =True)
    project_name = db.Column(db.Text, nullable=False, unique=True)
    # assignments = db.relationship('EmployeeProject', backref="project" )

class EmployeeProject(db.Model):
    __tablename__='employees_projects'
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.id'),primary_key = True)
    proj_code = db.Column(db.Text, db.ForeignKey('projects.proj_code'), primary_key=True)
    role = db.Column(db.Text)



def get_directory():
    all_emps = Employee.query.all()
    for emp in all_emps:
        if emp.department is not None:
            print (f"{emp.name} - {emp.department.dept_name} - {emp.department.phone}" )
        else:
            print(f"{emp.name}")

def get_directory_join():
    directory = db.session.query(Employee.name, 
                    Department.dept_name, 
                    Department.phone).join(Department).all()
    for name, dept, phone in directory:
        print(name, dept, phone)



def get_directory_join_class():
    directory = db.session.query(Employee, 
                    Department).join(Department).all()
    for emp, dept in directory:
        print(emp.name, dept.dept_name, dept.phone)


def get_directory_all_join():
    directory = db.session.query(Employee.name, 
                    Department.dept_name, Department.phone).outerjoin(Department).all()
    for name, dept, phone in directory:
        print(name, dept, phone)