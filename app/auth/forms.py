from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    
    email = StringField('Your Email Address',validators=[Required(),Email()])

    username = StringField('Enter your username',validators = [Required()])

    password = PasswordField('Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])

    confirm_password = PasswordField('Confirm Passwords',validators = [Required()])

    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])

    password = PasswordField('Password', validators = [Required()]) 
    
    remember = BooleanField('Remember Me ')

    submit = SubmitField('Log in ')
=======
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your Name',validators=[Required()])
    password = PasswordField('password',validators=[Required(),EqualTo('password_confirm',message = 'password must match')])
    password_confirm = PasswordField('confirm passwords',validators=[Required()])
    submit = SubmitField('sign Up')
    def validate_email(self,data_field):
    # method that checks if there is no user registered with given email
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')
    def validate_username(self,data_field):
    # method that checks if user name is unique
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')
class LoginForm(FlaskForm):
    email = StringField('your email adress',validators=[Required(),Email()])
    password = PasswordField('password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
