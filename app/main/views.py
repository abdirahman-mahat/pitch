from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm , CommentForm
from .. import db, photos
app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   title = "Pitch"
   '''
   title = 'Pitch'
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
        category=form.category.data
        

        pitch = Pitch(title=title, content=content,category=category)
        db.session.add(pitch)
        db.session.commit()

        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index', id=pitch.id))

    return render_template('new_pitch.html', title='New Post', pitch_form=form, post ='New Post')


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content,pitch_id=id)

        db.session.add(comment)
        db.session.commit()

    comment = Comment.query.filter_by(pitch_id=id).all()



    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/pitch_review/<int:id>',methods=['GET','POST'])
@login_required
def pitch_review(id):
    pitch=Pitch.query.get_or_404(id)
    comment= Review.query.all()
    form=ReviewForm()

    if request.args.get("like"):
        pitch.like = pitch.like+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_review/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislike=pitch.dislike+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_review/{pitch_id}".format(pitch_id=pitch.id))

    if form.validate_on_submit():
        review = form.review.data

        new_review = Review(id=id,review=review,user_id=current_user.id)

        new_review.save_review()
        return redirect(url_for('main.pitch_review',id=id))
    reviews = Review.query.all()
    return render_template('pitch_review.html',comment=comment,pitch=pitch,review_form=form,reviews=reviews)
