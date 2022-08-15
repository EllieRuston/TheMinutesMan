from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
#from .form import *
from .models import Note
from . import db
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import InputRequired
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    

            
    return render_template('home.html', user=current_user,)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId= note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
                        
    return jsonify({})

# class Action(Form):
#     action = StringField('action', validators=[InputRequired()])
#     person_R = StringField('person_R', validators=[InputRequired()])
#     deadline = DateField('deadline')
#     extra_data = StringField('extra_data')
    
# class Topic(Form):
#     topic = StringField('topic', validators=[InputRequired()])
#     raised_by = StringField('raised_b', validators=[InputRequired()])
#     actions = FieldList(FormField(Action), min_entries=3)
#     save = SubmitField('Save')
    
class Notes(FlaskForm):
    title= StringField('title', validators=[InputRequired()])
    start_T = StringField('start_T', validators=[InputRequired()])
    end_T = StringField('end_T', validators=[InputRequired()])
    a_present = TextAreaField('a_present', validators=[InputRequired()])
    a_absent = TextAreaField('a_absent')
    topic = StringField('topic', validators=[InputRequired()])
    raised_by = StringField('raised_b', validators=[InputRequired()])
    action = TextAreaField('action', validators=[InputRequired()])
    person_R = StringField('person_R', validators=[InputRequired()])
    deadline = DateField('deadline')
    extra_data = TextAreaField('extra_data')
    save = SubmitField('Save')

@views.route('/minutes', methods=['GET', 'POST'])
@login_required
def minutes():
    form = Notes()
      
    if request.method == 'POST':
        title = request.form.get('title')
        start_T = request.form.get('start_T')
        end_T = request.form.get('end_T')
        a_present = request.form.get('a_present')
        a_absent = request.form.get('a_absent')
        topic = request.form.get('topic')
        raised_by = request.form.get('raised_by')
        action = request.form.get('action')
        person_R = request.form.get('person_R')
        deadline = request.form.get('date')
        extra_data = request.form.get('extra_data')
        
        if form.validate_on_submit(): 
            new_note = Note(user_id=current_user.id, title=title, start_T=start_T, end_T=end_T, a_present=a_present, a_absent=a_absent, topic=topic, raised_by=raised_by, action=action, person_R=person_R, deadline=deadline, extra_data=extra_data )
            db.session.add(new_note)
            db.session.commit()
            flash(f'Minutes for {form.title.data} saved.', category='success')
            return redirect(url_for('views.home'))
        else:   
            for feild, errors in form.errors.items():
                for error in errors:
                    flash ("error in {}: {}".format(
                        getattr(form, feild).label.text,
                        error), category='error'
                    )
                    
            # flash(f'minutes are incomplete', 'error')
        
    return render_template('minutes.html', form=form, user=current_user )