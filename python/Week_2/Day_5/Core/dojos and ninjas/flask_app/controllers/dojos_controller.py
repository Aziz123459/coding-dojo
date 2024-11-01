from flask import session,request,render_template,redirect
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja
from flask_app import app


@app.route('/')
def get_dojos():
    list_dojos=Dojo.get_all()
    return render_template("dojos_form.html",list_dojos=list_dojos)
@app.route('/dojos',methods=["POST"])
def creat():
    new_dojo={
        "name":request.form["name"]
    }
    result=Dojo.creat(new_dojo)
    return redirect('/')
@app.route('/ninja')
def ninja():
    list_dojos=Dojo.get_all()
    return render_template("ninjas_form.html",list_dojos=list_dojos)
@app.route('/dojos/<int:id>')
def show(id):
    data={
        "id":id
    }
    list_ninjas=Dojo.show(data)
    return render_template("show_form.html",list_ninjas=list_ninjas)
