from flask import Blueprint, render_template

blue = Blueprint('blue01', __name__)

from App.model import Person, Student
from App.ext import  db


def init_view(app):
    app.register_blueprint(blue)


@blue.route('/hello/')
def hello_world():
    return render_template('index.html')

@blue.route('/addstu/')
def add_student():
    stu = Student()
    stu.name = 'haha'
    db.session.add(stu)
    db.session.commit()
    return 'sucess'


@blue.route('/deletestu/<int:id>/')
def delete_stu(id):
    stu = Student.query.get(id)
    db.session.delete(stu)
    db.session.commit()
    return 'delete done.'
