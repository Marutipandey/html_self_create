from flask import Flask
from flask_mail import  Mail,Message
app=Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='priyanka.k@zecdata.com'
app.config['MAIL_PASSWORD']='Priya@4321'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
mail=Mail(app)

print(mail)
@app.route("/")
def index():
    msg=Message('Hello',sender='priyanka.k@zecdata.com',recipients=['priyanka.k@zecdata.com'])
    msg.body="Hello Flask this message is sent form Flask-Mail"
    mail.send(msg)
    return "Message Sent"
if __name__=='__main__':
    app.run(debug=True)