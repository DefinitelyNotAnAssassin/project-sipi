
from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required
from ..models.chat import group, user
from ..extensions import db, login, current_user
from .form import CreateJoinForm, MessageForm


chat = Blueprint('chat', __name__, template_folder="./templates"
)





@chat.route("/createjoinroom")
@login_required
def createjoinroom():
  print(current_user)
  form = CreateJoinForm()
  return render_template("createjoinroom.html", form = form)


@chat.route("/join")
def join():
  print(current_user.username)
  return "something"


@chat.route('/room/<roomid>')
def chat_room(roomid):
  cursor = group.query.filter(group.groupid == roomid).first()
  if cursor:
    if current_user in cursor.participants:
      form = MessageForm()
      return render_template('chat.html', msg = cursor.message, form = form, roomid = roomid)
    else:
      flash("Not authorized")
      return redirect(url_for('chat.createjoinroom'))
  else:
    flash("Group doesn't exists")
    return redirect(url_for('chat.createjoinroom'))
  return "Unexpected error | Room"

