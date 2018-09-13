from flask import Flask
from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm
from .. import db, photos
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
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category_id=form.category_id.data
        pitch = Pitch(title=title,
                      content=content,
                      category_id=category_id,
                      user=current_user)

        db.session.add(pitch)
        db.session.commit()

        # pitch.save_pitch(pitch)
        
        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.single_pitch',id=pitch.id))

    return render_template('new_pitch.html', title='New Post', pitch_form=form, post ='New Post')