from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db,app
from flask import flash
from flask_bcrypt import Bcrypt
import re	# the regex module
# create a regular expression object that we'll use later
bcrypt=Bcrypt(app)   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Regist:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
    @classmethod
    def creat_one(cls,data):
        query="INSERT INTO regist(first_name,last_name,email,password)VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result=connectToMySQL(db).query_db(query,data)
        return(result)
    @staticmethod
    def validation( data ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!","email_validation")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("first name must be longer then 3","first_name_validation")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("last name must be longer then 3.","last_name_validation")
            is_valid = False
        if len(data['password']) < 8:
            flash("password must be longer then 8","password_validation")
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash("Passwords do not match.","password_confirmation")
            is_valid = False
        return is_valid
    @classmethod
    def get_one_by_email(cls,data):
        query="select * from regist where email=%(email)s;"
        result=connectToMySQL(db).query_db(query,data)
        if len(result)==0:
            flash("User email not found in the database","email_validation_login")
            return None
        else:
            current_user=Regist(result[0])
            return current_user
    @staticmethod
    def validation_password(hashed_password,plain_password):
        if (not bcrypt.check_password_hash(hashed_password,plain_password)):
            flash("wrong password","login_password_validation")
            return False
        else:
            return True