from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f'Username {username_to_check.data} is already exists.')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError(f'Email {email_to_check.data} is already exists.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Enter Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    username = StringField(label='Enter username:', validators=[DataRequired()])
    password = PasswordField(label='Enter Password:', validators=[DataRequired()])
    submit = SubmitField(label='Log in')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase')

class DiscardForm(FlaskForm):
    submit = SubmitField(label='Discard')