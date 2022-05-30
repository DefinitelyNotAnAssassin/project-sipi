from django.test import tag
from ..extensions import db


book_tag = db.Table('book_tag', 
db.Column('book', db.String, db.ForeignKey("books.bookname")),
db.Column('tag', db.String, db.ForeignKey('tags.tagname')), 

)



class Category(db.Model):
  __bind_key__ = "library"
  _id = db.Column("id", db.Integer, primary_key = True)
  book_category = db.Column("book_category", db.String)
  booklist = db.relationship('Books',lazy='dynamic', backref=db.backref('book_category', lazy='joined'))
  def __init__(self, book_category):
    self.book_category = book_category




class Tags(db.Model):
  __bind_key__ = "library"
  _id = db.Column("id", db.Integer, primary_key = True)
  tagname = db.Column('tagname', db.String)

  def __init__(self, tagname):
    self.tagname = tagname

class Books(db.Model):
  __bind_key__ = "library"
  _id = db.Column("id", db.Integer, primary_key = True)
  bookname = db.Column("bookname", db.String)
  filename = db.Column("filename", db.String)
  authorname = db.Column('authorname', db.String)
  year_published = db.Column("year_published", db.Integer)
  sourcelink = db.Column("sourcelink", db.String)
  category = db.Column(db.Integer, db.ForeignKey('category.book_category'))
  tag_name = db.relationship(Tags, secondary = book_tag, lazy = "dynamic", backref = "booklist")
  upload_date = db.Column('upload_date', db.Date)

  def __init__(self, bookname,filename, authorname, year_published, sourcelink, upload_date ):
    self.bookname = bookname
    self.filename = filename
    self.authorname = authorname
    self.year_published = year_published
    self.sourcelink = sourcelink
    self.upload_date = upload_date 

  
    