from flask import Flask, render_template
app=Flask(__name__)
@app.route('/hii')
def hello():
    return "hii fl3.py"
@app.route('/')
def hello1():
    return render_template('bootstrap.html')
app.run()
