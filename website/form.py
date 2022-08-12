from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import input_required 

class MinutesForm(FlaskForm):
    title= StringField('title', validators=[input_required()])
    date = DateField('date')
    start_T = TimeField('start_T', validators=[input_required()])
    end_T = TimeField('end_T', validators=[input_required()])
    a_present = StringField('a_present', validators=[input_required()])
    a_absent = StringField('a_absent')
    topic = StringField('topic', validators=[input_required()])
    raised_by = StringField('raised_b', validators=[input_required()])
    action = StringField('action', validators=[input_required()])
    person_R = StringField('person_R', validators=[input_required()])
    extra_data = StringField('extra_data')
    deadline = DateField('deadline')
    save = SubmitField('save')
    