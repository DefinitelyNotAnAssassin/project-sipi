
from flask import Blueprint, render_template, session, redirect, url_for
from .form import SearchForm
from ..models.library import Books
from ..extensions import login_required
library = Blueprint('library', __name__, template_folder="./templates")

@library.route("/")
def index():
    form = SearchForm()
    if "read_later" in session:
      readcount = len(session["read_later"])
      
    else:
      readcount = 0
    return render_template("index.html", form = form, count = readcount)


@library.route("/view")
def view():
  return render_template("view.html")


@library.route("/faq")
def faq():
  form = SearchForm()
  return render_template("faq.html", form = form)

@library.route("/readlist")
def readlist():
  if "read_later" in session:
    form = SearchForm()
    data = Books.query.filter(Books.bookname.in_(session["read_later"])).all()
    print(data)
    return render_template("readlist.html", data = data, form = form)
   
  elif "read_later" not in session:
    return redirect(url_for('library.index'))


@library.route("/feedback/<bookname>")
@login_required
def feedback(bookname):
  form = SearchForm()
  exists = Books.query.filter(Books.bookname == bookname).first()
  print(bookname)
  if exists:
    return render_template("feedback.html", bookname = bookname, form = form)
  else:
    return "Bookname doesn't exists"
  