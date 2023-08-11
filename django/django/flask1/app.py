from flask import Flask,request,flash,url_for,redirect,render_template
import flask
from flask_sqlalchemy import  SQLAlchemy
app=Flask("__name__")
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://students.sqlite3'
app.config['SECRET_KEY']="random string"
db=SQLAlchemy(app)
class students(db.Model):
    id=db.Column('student_id',db.integer,primary_key=True)
    name=db.column(db.string(100))
    city=db.column(db.string(100))
    addr=db.column(db.string(100))
    pin=db.column(db.string(100))
    def __init__(self,name,city,addr,pin):
        self.name=name
        self.city=city
        self.addr=addr
        self.pin=pin
@app.route('/')
def show_all():
    return render_template('show_all.html',students=students.query.all())
@app.route('/new',methods=('GET','POST'))
