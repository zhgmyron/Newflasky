# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name= StringField('what is you name?',validators=[Required()])
    sumbit = SubmitField('Sumbit')