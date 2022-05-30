
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import login_required
from ..user.form import LoginForm
from ..models.chat import user
from ..extensions import login_user, logout_user

login_api = Blueprint("login_api", __name__)

@login_api.route("/login_user", methods = ["POST"])
def loginuser():
  form = LoginForm()
  if form.validate_on_submit():
    userid = user.query.filter(user.username == form.Username.data).first()
    print(userid)
    if userid is None or not userid.check_password(form.Password.data):
      flash("Invalid Username / Password") 
      
      return render_template("login.html", form = form)
    else:
      login_user(userid)
      next = request.form.get("next")
      print(next)
      return redirect(next or "/")
  print(form.errors)
  return redirect(url_for('login'))

@login_api.route("/logout")
@login_required
def logout():
  logout_user()
  flash("User Logout")
  return redirect(url_for("user_route.login_user"))