from App.ext import db


class Person(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))


class Student(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(20))