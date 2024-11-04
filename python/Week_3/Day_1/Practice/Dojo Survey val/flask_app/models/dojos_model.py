from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
class Dojo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.location=data["location"]
        self.language=data["language"]
        self.comment=data["comment"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
    
    @classmethod
    def create(cls,data):
        query="insert into dojos(name,location,language,comment)values(%(name)s,%(location)s,%(language)s,%(comment)s);"
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result

    @staticmethod
    def validation(data):
        is_valid=True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("You must sent a comment.")
            is_valid = False
        return is_valid

    @classmethod
    def get_one(cls,data):
        query="select* from dojos where id=%(id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        dojo=Dojo(result[0])
        return dojo