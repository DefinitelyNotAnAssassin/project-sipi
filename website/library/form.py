from ..extensions import FlaskForm, StringField, SelectMultipleField, InputRequired, SelectField


class SearchForm(FlaskForm):
  Title = StringField('Title')
  Category = SelectField('Category', validators = [InputRequired()], choices =["General Works", "Archival Research Manuscript", "STEM"])
  #Tags = SelectMultipleField("Tags", choices=["Natural sciences & mathematics", 'Mathematics', 'Astronomy & Applied Science', 'Physics', 'Chemistry & Allied Sciences','Earth Sciences', "Paleontology, Paleonzology", "Life Sciences; Biology", "Plants(Botany)", "Animals(Zoology)"])
  Tags = SelectMultipleField("Tags", choices=["Natural sciences & mathematics", 'Mathematics', 'Astronomy & Applied Science', 'Physics', 'Chemistry & Allied Sciences','Earth Sciences', "Paleontology, Paleonzology", "Life Sciences; Biology", "Plants(Botany)", "Animals(Zoology)"])
  