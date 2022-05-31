from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class New_Astroid_Form(FlaskForm):
    ad = FloatField('ad',
    validators = [DataRequired()])
    q = FloatField('q',
    validators = [DataRequired()])
    a = FloatField('a',
    validators = [DataRequired()])
    e = FloatField('e',
    validators = [DataRequired()])
    dv = FloatField('dv',
    validators = [DataRequired()])
    per = FloatField('per',
    validators = [DataRequired()])
    moid = FloatField('moid',
    validators = [DataRequired()])
    diameter = FloatField('diameter',
    validators = [DataRequired()])
    submit = SubmitField('Submit')