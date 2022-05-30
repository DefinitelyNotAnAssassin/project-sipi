from ..extensions import StringField, PasswordField, EqualTo, Length, InputRequired, FlaskForm, SubmitField

class CreateJoinForm(FlaskForm):
  Room_Id = StringField('Room Id', validators = [InputRequired(), Length(min=4, max = 75)])
  Room_Code = StringField('Room Code', validators = [InputRequired(), Length(min=4, max = 75)])
  
class MessageForm(FlaskForm):
  Message = StringField("Message", validators = [InputRequired(), Length(max = 255)])
  Send_Message = SubmitField("Send")