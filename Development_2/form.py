from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class New_Astroid_Form(FlaskForm):
    ad = FloatField('ad',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    q = FloatField('q',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    a = FloatField('a',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    e = FloatField('e',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    dv = FloatField('dv',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    per = FloatField('per',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    moid = FloatField('moid',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    diameter = FloatField('diameter',
    validators = [DataRequired(),
    Length(min=2, max = 7)])
    submit = SubmitField('Submit')