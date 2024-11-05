from flask import session,request,render_template,redirect
from flask_app.models.regist_model import   Regist
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 


@app.route('/')
def temp():
    return render_template("regist&login_form.html")
@app.route('/register', methods=['POST'])
def register():
    data={
        **request.form
        
    }
    if  not Regist.validation(data):
        return redirect("/")
    hashed_password = bcrypt.generate_password_hash(data['password'])
    data['password'] = hashed_password
    Regist.creat_one(data)
    return redirect("/success")
@app.route('/success')
def registration():
    return render_template("success_form.html")
@app.route("/login",methods=["POST"])
def login_processing():
    data={
        "email":request.form["email"]
    }
    current_user=Regist.get_one_by_email(data)
    if current_user==None:
        return redirect("/")
    else:
        if not (Regist.validation_password(current_user.password,request.form["password"])):
            return redirect("/")
        else:
            session["id"]=current_user.id
            session["full_name"]=current_user.first_name+" "+current_user.last_name
            return redirect("/success")
@app.route("/logout")
def log_out():
    session.clear()
    return redirect('/')