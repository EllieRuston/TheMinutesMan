from . import db 
from flask import Blueprint, render_template, request, flash, redirect, url_for

from website import DB_NAME
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean =True)

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email=request.form.get('email')
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 char', category="error")
        elif len(username) < 2:
            flash('Username needs to be first and last name', category='error')
        elif password1 != password2:
            flash('passwords must match', category='error')
        elif len(password1) < 7:
            flash('passwords must be longer than 7 char', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password2, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created', category='success')
            return redirect(url_for('views.home'))
            #add user to database
            
    return  render_template('register.html')

