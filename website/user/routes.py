from .form import LoginForm
from flask import Blueprint, render_template
from ..models.chat import user
from ..extensions import bcrypt, db, login, current_user

user_route = Blueprint("user_route", __name__, template_folder="./templates")


@login.user_loader
def load_user(id):
    return user.query.get(int(id))
@user_route.route("/login")
def login_user():
    form = LoginForm()
    return render_template("login.html", form = form)


@user_route.route("/profile")
def profile():
  print(current_user.joined_group)
  return render_template("profile.html", grouplist = current_user.joined_group)
