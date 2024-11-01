from flask import session,request,render_template,redirect
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
from flask_app import app

@app.route('/ninja/add',methods=["POST"])
def new_ninjas():

    new_ninjas={
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojos"]
    }
    result=Ninja.create_one(new_ninjas)
    dojo_id=new_ninjas["dojo_id"]
    return redirect('/dojos/'+str(dojo_id))


