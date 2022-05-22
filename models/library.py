from ..extensions import db

class Category(db.Model):
  __bind_key__ = "library"
  _id = db.Column("id", db.Integer, primary_key = True)
  book_category = db.Column("book_category", db.String)
  booklist = db.relationship('Books',lazy='dynamic', backref=db.backref('book_category', lazy='joined'))
  def __init__(self, book_category):
    self.book_category = book_category
class Books(db.Model):
  __bind_key__ = "library"
  _id = db.Column("id", db.Integer, primary_key = True)
  bookname = db.Column("bookname", db.String)
  filename = db.Column("filename", db.String)
  category = db.Column(db.Integer, db.ForeignKey('category.book_category'))
  def __init__(self, bookname,filename):
    self.bookname = bookname
    self.filename = filename