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
    id=User.creat(new_user)
    return redirect('/show/'+str(id))
@app.route('/show/<int:id>')
def show(id):
    data={
        "id":id
    }
    user=User.show(data)
    return render_template("show.html",user=user)
@app.route('/delete/<int:id>',methods=["POST"])
def delete(id):
    data={
        "id":id
    }
    User.delete(data)
    return redirect('/')
@app.route('/update/users/<int:id>')
def update_users(id):
    data={
        "id":id
    }
    user=User.get_one(data)
    return render_template('update.html',user=user)
@app.route('/updated/<int:id>', methods=["POST"])
def updated(id):
    data={
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
    }
    User.update(data)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)