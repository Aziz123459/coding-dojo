from flask import Flask,render_template,session,redirect,request
from addusers import User
app=Flask(__name__)
app.secret_key='secret'
@app.route('/')
def users():
    list_of_users=User.get_all()
    return render_template("user.html",list_of_users=list_of_users)
@app.route("/user/form")
def aff_form():
    return render_template("addusers.html")
@app.route('/new',methods=['POST'])
def add_user():
    new_user={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    result=User.creat(new_user)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)