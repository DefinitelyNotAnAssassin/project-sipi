from flask import Blueprint, request, redirect, render_template, url_for, send_from_directory, abort, session
from ..extensions import json
from ..models.library import Books, Category
from ..library.form import SearchForm
import os

library_api = Blueprint('library_api', __name__)

@library_api.route("/get_title", methods = ["POST"])
def send_title():
  data = request.get_json()
  qry = Category.query.filter(Category.book_category == data['category']).first()
  qry = [(i.bookname) for i in qry.booklist.filter(Books.bookname.like(data["search"])).limit(10)]
  return json.dumps(qry)
  

@library_api.route("/search", methods = ["GET", "POST"])
def search():
  if request.method == "GET":
    return redirect(url_for("index"))
  elif request.method == "POST":
    form = SearchForm()
    if form.validate_on_submit():
      search = f"%{form.Title.data}%"
      result = Category.query.filter(Category.book_category == form.Category.data).first()
      return render_template("testresult.html", file = result.booklist.filter(Books.bookname.like(search)).limit(15))
    else:
      print(form.errors)
      return "Form Error!"


@library_api.route("/download/<path:path>")
def download(path):
  try:
    return send_from_directory(f"{os.getcwd()}/files/", path=path, as_attachment = True)
  except FileNotFoundError:
    abort(404)

@library_api.route("/addreadlist/<bookname>")
def addreadlist(bookname):
  if "read_later" not in session:
    session["read_later"] = []
  a = session["read_later"]
  a.append(bookname)
  session["read_later"] = a
  print(f"{bookname} Added to the session")
  return redirect(url_for("library.index"))
