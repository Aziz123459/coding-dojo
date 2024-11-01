from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas_model import Ninja
class Dojo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data['name']
        self.created_at=data["created_at"]
        self.updated_at=data['updated_at']
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        list_dojos=[]
        for data in result:
            list_dojos.append(Dojo(data))
        return list_dojos
    @classmethod
    def creat(cls,data):
        query="insert into dojos (name) values(%(name)s)"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return result
    @classmethod
    def show(cls,data):
        query="SELECT * FROM dojos join  ninjas on ninjas.dojo_id=dojos.id where dojos.id=%(id)s;"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        dojo=cls(result[0])
        dojo.ninjas=[]
        for data in result:
            ninja={
                **data,
                "id":data['ninjas.id'],
                "created_at":data['ninjas.created_at'],
                "updated_at":data['ninjas.updated_at']

            }

            dojo.ninjas.append(Ninja(ninja))
        return dojo