from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():
    fruits=['mango','apple','orange','banana']
    return render_template('home.html',hii='thid ifff ggff ddf',fru=fruits)

@app.route('/about')
def about():
       return '<h1>this is a about</h1>'

@app.route('/home')
def home():
       return '<h1>this is a home</h1>'
app.run()


