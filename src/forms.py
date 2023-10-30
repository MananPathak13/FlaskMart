from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')

class CheckoutForm(FlaskForm):
    stripe_token = StringField('Stripe Token', validators=[DataRequired()])
    submit = SubmitField('Purchase')
