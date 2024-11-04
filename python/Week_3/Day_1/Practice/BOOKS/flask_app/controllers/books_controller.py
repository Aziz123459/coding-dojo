from flask import session,request,render_template,redirect
from flask_app.models.authors_model import Authors
from flask_app.models.books_model import Books
from flask_app.controllers import authors_controller
from flask_app import app

@app.route('/books')
def get_books():
    list_books=Books.get_all()
    return render_template("books_form.html",list_books=list_books)
@app.route("/new",methods=["POST"])
def creat_book():
    new_book={
        "title":request.form["title"],
    }
    Books.creat(new_book)
    return redirect('/books')
@app.route('/autrhors/<int:id>')
def show_favorates(id):
    data={
        "id":id
    }
    list_favorates=Books.get_favorates(data)
    books=Books.get_all()
    return render_template("books_show_form.html",list_favorates=list_favorates,books=books)
@app.route("/add",methods=["POST"])
def add_book(id):
    add_book={
        "id":id,
        "title":request.form["title"]
    }
    Books.creat(add_book)
    return redirect('/autrhors/<int:id>')