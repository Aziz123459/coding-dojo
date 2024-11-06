from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self,data):
        self.id=data["id"]
        self.email=data["email"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def get_all(cls):
        query="select * from emails;"
        result=connectToMySQL(DATABASE).query_db(query)
        list_of_emails=[]
        for email in result:
            list_of_emails.append(Email(email))
        return list_of_emails

    @classmethod
    def create_one(cls,data):
        query="insert into emails (email) values (%(email)s);"
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @staticmethod
    def validate(data):
        is_valid=True
        if not EMAIL_REGEX.match(data["email"]):
            flash("invalid email address")
            is_valid=False
        return is_valid

    @classmethod
    def delete_one(cls,data):
        query="delete from emails where id=%(id)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query="select * from emails where email=%(email)s;"
        result=connectToMySQL(DATABASE).query_db(query,data)
        if len(result)==0:
            return True
        else:
            flash("The email address is already in the data base")
            return False
