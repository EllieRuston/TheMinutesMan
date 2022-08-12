from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import InputRequired


class MinutesForm(FlaskForm):
    title= StringField('title', validators=[InputRequired()])
    date = DateField('date')
    start_T = TimeField('start_T', validators=[InputRequired()])
    end_T = TimeField('end_T', validators=[InputRequired()])
    a_present = StringField('a_present', validators=[InputRequired()])
    a_absent = StringField('a_absent')
    topic = StringField('topic', validators=[InputRequired()])
    raised_by = StringField('raised_b', validators=[InputRequired()])
    action = StringField('action', validators=[InputRequired()])
    person_R = StringField('person_R', validators=[InputRequired()])
    extra_data = StringField('extra_data')
    deadline = DateField('deadline')
    save = SubmitField('Save')
    