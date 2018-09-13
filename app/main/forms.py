from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category= SelectField('Pitch Category', choices=[('Select a category', 'Select a category'),('Business', 'Business'),('Science and Tech', 'Science and Tech'),('Interview Pitch', 'Interview Pitch')])
    content = TextAreaField('The pitch...')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    title = StringField('Comment Title')
    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you...')
    submit = SubmitField('Submit')