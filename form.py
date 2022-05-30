from unicodedata import category
from click import option
from website.models.library import Tags
from website.extensions import FlaskForm, StringField, SelectField, SubmitField, InputRequired, FileRequired, FileField, FileAllowed, SelectMultipleField
class UploadForm(FlaskForm):
    Bookname = StringField("Bookname", validators = [InputRequired()])
    Authorname = StringField("Authorname", validators = [InputRequired()])
    Sourcelink = StringField("Sourcelink", validators = [InputRequired()])
    YearPublished = StringField("Year Published", validators = [InputRequired()])
    #Tags = SelectMultipleField("Tags", choices=["Natural sciences and mathematics", "Mathematics", "Physics"])
    Tags = SelectMultipleField("Tags", choices=["Natural sciences & mathematics", 'Mathematics', 'Astronomy & Applied Science', 'Physics', 'Chemistry & Allied Sciences','Earth Sciences', "Paleontology, Paleonzology", "Life Sciences; Biology", "Plants(Botany)", "Animals(Zoology)"])
    File = FileField("File", validators=[FileRequired(), FileAllowed(['pdf', '.pdf'], 'PDF Files Only')])
    Category = SelectField("Category", validators = [InputRequired()], choices=["General Works", "Archival Research Manuscript", "STEM"])