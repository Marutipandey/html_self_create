
from flask_wtf import Form
from wtforms.fields import TextField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField

from wtforms.fields import  validators,ValidationError
class ContactForm(Form):
    name=TextField("Name of student",[validators.Required("please enter your name.")])
    Gender=RadioField('Gender',choice=[('M','Male'),('F','Female')])
    Address=TextAreaField("Address")
    email=TextField("Email",[validators.Required("please enter your email address."),validators.Email("please enter your email")])
    Age=IntegerField("age")
    language=SelectField('Languages',choice=[('cpp','c++'),('py','python')])
    submit=SubmitField("send")
