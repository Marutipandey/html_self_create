from flask import Flask,session,redirect,url_for,render_template,request
app=Flask(__name__)
app.secret_key='any random string'
@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return 'Logged in as '+ username +'<br>'+ \
            "<br><a href='/logout'>click here to log out<a/></b>"
    return "You are not logged in <br><a href='/login'></br>" + \
        "click here to log in</b></a>"


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    #reove the username from the session if it is there
    session.pop('username',None)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
