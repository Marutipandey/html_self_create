from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='postgresql+psycopg2://postgres:password@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class favourites(db.Model):
   id=db.Column(db.integer,primary_key=True)
   auther=db.Column(db.String(30))
   quotes=db.Column(db.String(2000))



@app.route('/')
def index(): 
    result=favquotes.oquery.all() 
    return render_template('about.html',result=result)

@app.route('/hom')
def hom():
        return render_template('quotes.html')

@app.route('/about')
def about():
       return '<h1>this is a about</h1>'

@app.route('/home')
def home():
       return '<h1>this is a home</h1>'
app.run()

@app.route('/process',method=['post'])
def process():
       auther=request.form['auther']
       quotes=request.form['quotes']
       quotedata=Favquotes(auther=auther,quotes=quotes)
       #return redirect(url_for('about.html'))
       db.create_session.add(quotedata)
       


