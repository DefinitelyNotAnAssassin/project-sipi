from ..extensions import FlaskForm, StringField, SelectMultipleField, InputRequired


class SearchForm(FlaskForm):
  Title = StringField('Title')
  Category = SelectMultipleField('Category', validators = [InputRequired()], choices =['General Works, Computer Science & Information','Philosophy & Psychology', 'Religion', "Social Sciences", "Language", "Science", "Technology","Arts & Recreation", "Literature", "History & Geography"])


