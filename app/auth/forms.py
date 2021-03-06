# -*- coding: UTF-8 -*-
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError

from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),
                                            Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    sumbit = SubmitField('Login')


class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),
                                            Email()])
    username = StringField('Username', validators=[Required(),Length(1,64),
                                                   Regexp])
    password = PasswordField('Password',validators=[Required(),
                                    EqualTo('password2',message='Passwords must match.')])
    password2= PasswordField('Confirm password',validators=[Required()])
    submit= SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')