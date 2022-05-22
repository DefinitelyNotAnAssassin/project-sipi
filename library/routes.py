
from flask import Blueprint, render_template, session, redirect, url_for
from .form import SearchForm
from ..models.library import Books
library = Blueprint('library', __name__, template_folder="./templates")

@library.route("/")
def index():
    form = SearchForm()
    return render_template("index.html", form = form)


@library.route("/view")
def view():
  return render_template("view.html")


@library.route("/faq")
def faq():
  return render_template("faq.html")

@library.route("/readlist")
def readlist():
  if "read_later" in session:
    data = Books.query.filter(Books.bookname.in_(session["read_later"])).all()
    print(data)
    return render_template("readlist.html", data = data)
   
  elif "read_later" not in session:
    return redirect(url_for('library.index'))

