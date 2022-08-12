from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#login 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success') 
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')  
        else:
            flash('Email does not exist, complete registration.', category='error')
    
    return render_template("login.html", user=current_user)

#logout 
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# register 
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email=request.form.get('email')
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        user= User.query.filter_by(email=email).first()
        if user:
            flash('Account with this email already exits', category='error')
        elif len(email) < 4:
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
            login_user(new_user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
            #add user to database
            
    return render_template('register.html', user=current_user)

