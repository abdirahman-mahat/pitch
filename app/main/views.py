from flask import Flask
from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import User, Pitch, Comment
from .forms import UpdateProfile

app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   title = "Pitch Perfect"
   '''
   title = 'Pitch Perfect'
   pitchs = Pitch.query.all()

   return render_template('index.html', title= title, pitchs = pitchs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)