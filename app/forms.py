from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, length, InputRequired, NumberRange
from wtforms import SelectField, TextAreaField, DecimalField
from wtforms.validators import EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    fullName = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password',
                              validators=[DataRequired(), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class PropertyForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    landlord_name = StringField('Address', validators=[DataRequired()])
    property_type = SelectField('Property Type',
                                choices=[('duplex', 'Duplex'), ('bungalow', 'Bungalow'), ('apartment', 'Apartment')],
                                validators=[InputRequired()])
    number_of_beds = SelectField('Number of Beds',
                                 choices=[('selfcontain', 'Self-Contain'), ('1', '1'), ('2', '2'), ('3', '3'),
                                          ('4', '4'), ('5', '5'), ('other', 'Other')], validators=[InputRequired()])
    location = StringField('Property Address', validators=[DataRequired()])
    state = SelectField('State', choices=[('Oyo', 'Oyo')], validators=[InputRequired()])
    lga = SelectField('Local Government Area',
                      choices=[
                          ('Afijio', 'Afijio'), ('Akinyele', 'Akinyele'), ('Atiba', 'Atiba'), ('Atisbo', 'Atisbo'),
                          ('Egbeda', 'Egbeda'), ('Ibadan North', 'Ibadan North'),
                          ('Ibadan North-East', 'Ibadan North-East'),
                          ('Ibadan North-West', 'Ibadan North-West'), ('Ibadan South-East', 'Ibadan South-East'),
                          ('Ibadan South-West', 'Ibadan South-West'), ('Ibarapa Central', 'Ibarapa Central'),
                          ('Ibarapa East', 'Ibarapa East'), ('Ibarapa North', 'Ibarapa North'), ('Ido', 'Ido'),
                          ('Irepo', 'Irepo'), ('Iseyin', 'Iseyin'), ('Itesiwaju', 'Itesiwaju'), ('Iwajowa', 'Iwajowa'),
                          ('Kajola', 'Kajola'), ('Lagelu', 'Lagelu'), ('Ogbomoso North', 'Ogbomoso North'),
                          ('Ogbomoso South', 'Ogbomoso South'), ('Ogo Oluwa', 'Ogo Oluwa'), ('Oluyole', 'Oluyole'),
                          ('Ona Ara', 'Ona Ara'), ('Orelope', 'Orelope'), ('Ori Ire', 'Ori Ire'),
                          ('Oyo East', 'Oyo East'),
                          ('Oyo West', 'Oyo West'), ('Saki East', 'Saki East'), ('Saki West', 'Saki West'),
                          ('Surulere', 'Surulere')
                      ], validators=[InputRequired()])
    street = StringField('Street Name')
    price = DecimalField('Price', validators=[InputRequired(), NumberRange(min=100000, max=1000000)])
    youtube_links = TextAreaField('Youtube Video Links')
    image_upload = FileField('Upload Images')
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    desired_location = StringField('Desired Location', validators=[DataRequired()])
    submit = SubmitField('Search')