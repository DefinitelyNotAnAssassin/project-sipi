from flask_sqlalchemy import SQLAlchemy
from flask import *
from form import UploadForm
from website.models.library import Books, Tags, Category
from website import create_app
from website.extensions import db, os
import uuid
import datetime
app = Flask(__name__)

db.init_app(app)

app.secret_key = 'Secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///C:\\Users\Winmri\Desktop\\project-sipi-master\website\\library.sqlite3"
app.config["SQLALCHEMY_BINDS"] = {
    "library": r"sqlite:///C:\\Users\\Winmri\Desktop\\project-sipi-master\website\\library.sqlite3"
}
@app.route("/")
def index():
    form = UploadForm()
    return render_template("upload.html", form = form)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/addbook", methods = ["POST"])
def addbook():
    form = UploadForm()
    if form.validate_on_submit():
        random = uuid.uuid4()
        add_book = Books(form.Bookname.data,f"{random}.pdf" , form.Authorname.data, form.YearPublished.data, form.Sourcelink.data, datetime.datetime.now() )
        tagsqry = Tags.query.filter(Tags.tagname.in_(form.Tags.data)).all()
        catqry = Category.query.filter(Category.book_category == form.Category.data).first()
        catqry.booklist.append(add_book)
        db.session.add(add_book)
        for i in tagsqry:
            add_book.tag_name.append(i)
            
        file = form.File.data
        file.save(os.path.join(f"{os.getcwd()}/website/file", f"{random}.pdf"))
        

        db.session.commit()


        return "Book added"

    else:
        print(form.errors)
        return "Form error"
    return "TODO"

@app.route("/register_user")
def register_user():
    return "TODO"

@app.route("/adduser", methods = ["POST"])
def adduser():
    return "TODO"

@app.route("/test")
def test():
    data = Category.query.all()
    for i in data:
        print(i.book_category)

    data2 = Tags.query.all()
    for i in data2:
        print(i.tagname)
    
    data3 = Books.query.all()
    
    return "TODO"

