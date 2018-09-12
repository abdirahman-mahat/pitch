from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category_id = SelectField('Pitch Category', choices=[('Select a category', 'Select a category'),('Business', 'Business'),('Science and Tech', 'Science and Tech'),('Interview Pitch', 'Interview Pitch')])
    content = TextAreaField('The pitch...')
    submit = SubmitField('Submit')

