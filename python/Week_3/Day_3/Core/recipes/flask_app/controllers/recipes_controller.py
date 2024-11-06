from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.recipes_model import Recipe
from flask_app.models.user_model import User




@app.route('/recipes')
def dashboard():
    if'user_id' not in session:
        return redirect('/')
    user=User.get_by_id({'id':session['user_id']})
    recipes =Recipe.get_all()
    return render_template("dashboard.html",user=user,recipes=recipes)
@app.route("/recipes/new")
def new_recipe():
    if 'user_id' not in session :
        return redirect('/')
    return render_template('new_recipes.html')
@app.route('/recipes/create', methods=["POST"])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    
    if Recipe.validate(request.form):
        data={**request.form,'user_id':session["user_id"]}
        Recipe.create(data)
        return redirect('/recipes')
    return redirect('/recipes/new')
@app.route('/recipes/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        "id":id
    }
    user=User.get_by_id({'id':session['user_id']})
    recipe=Recipe.get_by_id(data)
    return render_template("view.html",recipe=recipe,user=user)
@app.route("/recipes/<int:id>/delete")
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        "id":id
    }
    Recipe.delete(data)
    return redirect('/recipes')
@app.route("/recipes/edit/<int:id>")
def update_form(id):
    data={
        "id":id
    }
    recipe=Recipe.get_by_id(data)
    return render_template("update_form.html",recipe=recipe)
@app.route("/recipes/update/<int:id>",methods=["POST"])
def update_recipes(id):
    if Recipe.validate(request.form):
        data={
            **request.form,
            "id": id
        }
        Recipe.update(data)
        return redirect("/recipes")
    return redirect(f'/recipes/edit/{id}')
