<<<<<<< HEAD
from .. import db
from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from flask_login import login_user, logout_user,  login_required
from .forms import RegistrationForm, LoginForm
from ..email import mail_message


=======
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from . import auth
from ..email import mail_message
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
<<<<<<< HEAD
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    form = LoginForm()
    title = "pitch perfect login"
    return render_template('auth/login.html',login_form = login_form,title=title)

=======
        user = User.query.filter_by(email = login_form.email.data),first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))
        flash('Invalid username or password')
    title = "pitch Login"
    return render_template('auth/login.html',login_form=login_form,title=title)
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
<<<<<<< HEAD

        mail_message("Welcome to Pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/auth/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for("main.index"))
=======
        mail_message("Welcome to pitch","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
    
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
