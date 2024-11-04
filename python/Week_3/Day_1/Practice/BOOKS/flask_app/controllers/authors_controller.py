from flask import session,request,render_template,redirect
from flask_app.models.authors_model import Authors
from flask_app.controllers import books_controller
from flask_app import app

@app.route("/")
def home():
    return redirect("/authors")
@app.route("/authors")
def get_authors():
    list_authors=Authors.get_all()
    return render_template("authors_form.html",list_authors=list_authors)
@app.route("/",methods=["POST"])
def creat_author():
    new_author={
        "full_name":request.form["full_name"]
    }
    Authors.creat(new_author)
    return redirect('/authors')

