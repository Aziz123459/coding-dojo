from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.authors_model import Authors
from flask_app import db


class Books:
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.creat_at=data["creat_at"]
        self.updates_at=data['updates_at']
    @classmethod
    def get_all(cls):
        query="select* from books;"
        result=connectToMySQL(db).query_db(query)
        list_books=[]
        for data in result:
            list_books.append(Books(data))
        return list_books
    @classmethod
    def creat(cls,data):
        query="insert into books (title) values(%(title)s);"
        result=connectToMySQL(db).query_db(query,data)
        return result
    @classmethod
    def get_favorates(cls,data):
        query="SELECT * FROM books join favorites ON favorites.book_id=books.id where favorites.author_id=%(id)s;"
        result=connectToMySQL(db).query_db(query,data)
        list_favorates=[]
        for data in result:
            list_favorates.append(Books(data))
        return list_favorates
    @classmethod
    def add_book(cls,data):
        query="insert into favorites (book_id,author_id) values(,5);"
        result=connectToMySQL(db).query_db(query,data)
        print (result)
        return result