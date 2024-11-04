from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db

class Authors:
    def __init__(self,data):
        self.id=data['id']
        self.full_name=data['full_name']
        self.creat_at=data["creat_at"]
        self.updated_at=data['updated_at']
    @classmethod
    def get_all(cls):
        query="select* from authors;"
        result=connectToMySQL(db).query_db(query)
        list_authors=[]
        for data in result:
            list_authors.append(Authors(data))
        return list_authors
    @classmethod
    def creat(cls,data):
        query="insert into authors (full_name) values(%(full_name)s);"
        result=connectToMySQL(db).query_db(query,data)
        return result
