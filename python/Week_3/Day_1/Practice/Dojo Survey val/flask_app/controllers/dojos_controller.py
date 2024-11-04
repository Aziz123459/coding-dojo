from flask import session,request,render_template,redirect
from flask_app.models.dojos_model import Dojo
from flask_app import app
@app.route('/')
def render():
    return render_template('index.html')

@app.route("/result/<int:id>")
def result(id):
    data={
        "id":id
    }
    dojo=Dojo.get_one(data)
    return render_template("result.html",dojo=dojo)  

@app.route("/submit",methods=["POST"])
def submit():
    data={
        **request.form
    }
    if  not Dojo.validation(data):
        return redirect("/")
    id=Dojo.create(data)
    return redirect("/result/"+str(id))
