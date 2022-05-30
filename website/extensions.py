from flask_sqlalchemy import SQLAlchemy
from wtforms import SelectField, StringField, PasswordField, SubmitField, SelectMultipleField
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import InputRequired, EqualTo, Length
import json
import os
from sqlalchemy import and_, or_
from flask_login import LoginManager, current_user, logout_user, login_user, login_required, UserMixin 
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, emit, join_room, leave_room
import time

db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
socketio = SocketIO()
