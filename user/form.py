from ast import Pass
from ..extensions import FlaskForm, StringField, InputRequired, PasswordField

class LoginForm(FlaskForm):
    Username = StringField("Username", validators=[InputRequired()])
    Password = PasswordField("Password", validators=[InputRequired()])