from flask import Blueprint, redirect, url_for, flash 
from ..extensions import db, and_, current_user 
from ..chat.form import CreateJoinForm
from ..models.chat import group



chat_api = Blueprint("chat_api", __name__)

#Create_Room 

@chat_api.route("/create_room", methods = ["POST"])
def create_room():
  form = CreateJoinForm()
  if form.validate_on_submit():
    group_exist = group.query.filter(group.groupid == form.Room_Id.data).first()
    if not group_exist:
      addGroup = group(form.Room_Id.data, form.Room_Code.data)
      db.session.add(addGroup)
      current_user.joined_group.append(group.query.filter(group.groupid == form.Room_Id.data).first())
      db.session.commit()
      flash("Group Created!")
      return redirect(url_for('chat.createjoinroom'))
      
    else:
      flash("Room already exists")
      return redirect(url_for('chat.createjoinroom'))
    
    
  else:
    flash("Invalid Form")
    return redirect(url_for('chat.createjoinroom'))
  
  return "???"


#Join Room
@chat_api.route("/join_room", methods = ["POST"])
def joinroom():
  form = CreateJoinForm()
  if form.validate_on_submit():
    cursor = group.query.filter(and_(group.groupid == form.Room_Id.data, group.password == form.Room_Code.data)).first()
    if cursor:
      if current_user in cursor.participants:
        return redirect(url_for('chat', roomid = form.Room_Id.data))
      else:
        cursor.participants.append(current_user)
        db.session.commit()
        return redirect(url_for('chat', roomid = form.Room_Id.data))
    else:
      flash("Room doesn't exists")
      return redirect(url_for('index'))
  else:
    print(form.errors)
    flash('Invalid Form')
    return redirect(url_for("index"))
  return "Unexpected Error | Join Room"


