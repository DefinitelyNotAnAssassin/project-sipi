from ..extensions import FlaskForm, StringField, SelectField, InputRequired


class SearchForm(FlaskForm):
  Title = StringField('Title',validators =[InputRequired()])
  Category = SelectField('Category', validators = [InputRequired()], choices =['General Works, Computer Science & Information','Philosophy & Psychology', 'Religion', "Social Sciences", "Language", "Science", "Technology","Arts & Recreation", "Literature", "History & Geography"])


