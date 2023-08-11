from flask import Flask, render_template 
app=Flask(__name__)

@app.route('/')
def hello_world():
    name="Priya"
    return render_template("home.html",names=name)
@app.route('/hello')
def hello_world1():
    return "hello hari bhai"
app.run(debug=True)
