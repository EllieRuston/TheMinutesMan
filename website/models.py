from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    m_deatils = db.relationship('M_details')
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class M_details (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(25), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    start_T = db.Column(db.DateTime(5), nullable=False)
    end_T = db.Column(db.DateTime(5), nullable=False)
    a_present = db.Column(db.String(), nullable=False)
    a_absent = db.Column(db.String(), nullable=False)
    m_topic = db.relationship('M_topic')
    
class M_topic(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    min_ID = db.Column(db.Integer, db.ForeignKey('M_details.id'))
    topic = db.Column(db.String(50), nullable=True)
    raised_by = db.Column(db.String(), nullable=False)
    m_action = db.relationship('M_action')
    
class M_action(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    topic_ID = db.Column(db.Integer, db.ForeignKey('M_topic.id'))
    action = db.Column(db.String(), nullable=False)
    person_R = db.Column(db.String(), nullable=False)
    extra_data = db.Column(db.String(), nullable=True)
    deadline = db.Column(db.DateTime(), nullable=False) 