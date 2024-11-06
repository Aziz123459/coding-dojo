from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Recipe : 
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date=data['date']
        self.duration=data['duration']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.poster=""

    @classmethod
    def create(cls,data):
        query="insert into recipes (name,description,instructions,date,duration,user_id) values (%(name)s,%(description)s,%(instructions)s,%(date)s,%(duration)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all(cls):
        query="select * from recipes join users on recipes.user_id=users.id;"
        result=connectToMySQL(DATABASE).query_db(query)
        all_recipes=[]
        for row in result:
            recipe =cls(row)
            recipe.poster=f"{row['first_name']} {row['last_name']}"
            all_recipes.append(recipe)
        return all_recipes
    @classmethod
    def get_user_recipes(cls,data):
        query="select * from recipes where users.id=%(user_id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        all_recipes=[]
        for row in result:
            all_recipes.append(cls(row))
        return all_recipes
    @classmethod
    def get_by_id(cls,data):
        query="select *from recipes join users on recipes.user_id=users.id where recipes.id=%(id)s; "
        result=connectToMySQL(DATABASE).query_db(query,data)
        recipe=cls(result[0])
        recipe.poster=result[0]['first_name']+" "+result[0]['last_name']
        return recipe
    
    
    # update
    @classmethod
    def get_one(cls,data):
        query="select * from recipes where id=%(id)s"
        result=connectToMySQL(DATABASE).query_db(query,data)
        recipe=Recipe(result[0])
        return recipe
    @classmethod
    def update(cls,data):
        query="update recipes set name=%(name)s ,description=%(description)s,instructions=%(instructions)s,date=%(date)s,duration=%(duration)s where id=%(id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    # end update
    @classmethod
    def delete(cls,data):
        query="DELETE from recipes where id=%(id)s"
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['name'])<3:
            is_valid=False
            flash("name too short","name")
        if len(data['description'])<3:
            is_valid=False
            flash("description too short","name")
        if len(data['instructions'])<3:
            is_valid=False
            flash("instructions  too short","instructions")
        if data['date']=="":
            is_valid=False
            flash("date is required","date")
        return is_valid
