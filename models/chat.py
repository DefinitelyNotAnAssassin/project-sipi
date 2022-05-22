from ..extensions import db, UserMixin, bcrypt

user_group = db.Table('user_group', 
db.Column('usermame', db.String, db.ForeignKey("user.usernames")),
db.Column('group', db.String, db.ForeignKey('group.groupid')), 

)



class group(db.Model):
  __bind_key__ = "chat"
  _id = db.Column("id", db.Integer, primary_key = True)
  groupid = db.Column("groupid", db.String(255))
  password = db.Column("password", db.String(255))
  message = db.relationship('message', backref = "groupid")

  def __init__(self, groupid, password):
    self.groupid = groupid
    self.password = password
class message(db.Model):
  __bind_key__ = "chat"
  _id = db.Column("id", db.Integer, primary_key = True)
  sender = db.Column("sender", db.String)
  content = db.Column("content", db.String(255))
  receiver = db.Column(db.String, db.ForeignKey('group.groupid'))
  def __init__(self, sender, content):
    self.sender = sender
    self.content = content
class user(UserMixin, db.Model):
  __bind_key__ = "chat"
  _id = db.Column("id", db.Integer, primary_key = True)
  username = db.Column("usernames", db.String(255))
  password = db.Column("password", db.String(255))
  joined_group = db.relationship(group, secondary = user_group, backref = "participants")

  def __init__(self, username, password):
    self.username = username
    self.password = password 
    
  def get_id(self):
    return (self._id)
  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)