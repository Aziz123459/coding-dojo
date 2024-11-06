from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def index ():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def regist():
    if  User.validation(request.form):

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data={
            **request.form,'password':pw_hash
            
        }
        
        user_id=User.create(data)
        current_user=User.get_by_id({"id":user_id})
        session['name']=current_user.first_name
        session['user_id']=user_id
        return redirect("/dashboard")
    return redirect('/')
@app.route("/login",methods=["POST"])
def login_processing():
    data={
        "email":request.form["email"]
    }
    user_in_db = User.get_by_email(data)
        # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email","email_validation_login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password","login_password_validation")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    current_user=User.get_by_id({"id":user_in_db.id})
    session['name']=current_user.first_name
        # never render on a post!!!
    return redirect("/dashboard")
@app.route("/dashboard")
def success():
    if 'user_id' not in session:
        return redirect('/')
    return render_template ("success.html")




@app.route("/logout")
def log_out():
    session.clear()
    return redirect('/')