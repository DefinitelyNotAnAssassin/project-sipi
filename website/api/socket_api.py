from flask import Blueprint
from ..extensions import socketio, emit, leave_room, join_room, current_user, db
from ..models.chat import user, group, message


socket_api = Blueprint("socket_api", __name__)

@socketio.on('room_connect')
def room_connect(roomid):
  join_room(roomid["roomid"])


def save_message(msg):
  groupid = group.query.filter(group.groupid == msg["roomid"]).first()
  save = message(msg["sender"],msg["content"])
  db.session.add(save)
  groupid.message.append(save)
  db.session.commit()
  
  

@socketio.on("send_message")
def send_message(message):
  print(message)
  message["sender"] = current_user.username
  emit('add_element', message, to = message["roomid"], broadcast = True)
  save_message(message)

