from models import Employee, Department, db, connect_db, Project, EmployeeProject
from app import app

db.drop_all()
db.create_all()


dungeon = Department(dept_code='dung', dept_name='dungeon', phone='650-876-6543')
wizardy = Department(dept_code='wiz', dept_name='wizardy', phone='650-876-6542')
battle = Department(dept_code='bat', dept_name='battle')
sales =  Department(dept_code='sal', dept_name='sales')
ring = Project( proj_code='rng', project_name='Fight Sauron', )
chaos = Project(proj_code='cha', project_name='War of Chaos')
 




sigmar = Employee(name='Sigmar',state='OW',dept_code='bat')
harry = Employee(name='Harry Potter',state='HOG',dept_code='wiz')
aragorn = Employee(name='Aragorn Son of Arathorn',state='ME',dept_code='bat')
orc = Employee(name='Thraka',state='WAR',dept_code='dung')
saruman = Employee(name='Sarumon',state='ME',dept_code='wiz')
karl = Employee(name='Karl Franz',state='EMP',dept_code='bat')
archaon = Employee(name='Archaon',state='CHA',dept_code='dung')
snape = Employee(name='Snape',state='HOG',dept_code='wiz')
Gotr = Employee(name='Gotrek',state='EMP',dept_code='bat')
gandy = Employee(name='Gandalf',state='ME',dept_code='wiz')
batman = Employee(name='batman',state='GC')



db.session.add(dungeon)
db.session.add(wizardy)
db.session.add(battle)
db.session.add(sales)
db.session.add(ring)
db.session.add(chaos)
db.session.commit()


db.session.add(aragorn)
db.session.add(orc)
db.session.add(gandy)
db.session.add(harry)
db.session.add(sigmar)
db.session.add(snape)
db.session.add(karl)
db.session.add(archaon)
db.session.add(Gotr)
db.session.add(saruman)
db.session.add(batman)

employee_proj3 = EmployeeProject(emp_id=7, proj_code='cha',role='emperor')
employee_proj4 = EmployeeProject(emp_id=8, proj_code='cha',role='warlord')
employee_proj5 = EmployeeProject(emp_id=9, proj_code='cha',role='slayer')

employee_proj = EmployeeProject(emp_id=3, proj_code='rng',role='wizard')
employee_proj2 = EmployeeProject(emp_id=1, proj_code='rng',role='ranger')
db.session.add(employee_proj5)
db.session.add(employee_proj4)
db.session.add(employee_proj3)
db.session.add(employee_proj)
db.session.add(employee_proj2)
db.session.commit()

