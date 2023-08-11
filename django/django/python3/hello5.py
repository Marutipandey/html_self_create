from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return '<h1> hello hii hgf ddf dedff <h1>'

@app.route('/home')
def home():
    return '<h1> hello hii hgf ddf dedff <h1>'
app.run()