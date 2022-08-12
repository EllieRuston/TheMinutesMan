from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .form import MinutesForm
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Notes are too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
            
    return render_template('home.html', user=current_user)

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

@views.route('/minutes', methods=['GET', 'POST'])
def minutes():
    form = MinutesForm()
    if form.validate_on_submit():
        flash(f'Minutes for {form.title.data} saved.', 'success')
        return render_template(url_for('home'))
    
    return render_template('minutes.html', form=form)