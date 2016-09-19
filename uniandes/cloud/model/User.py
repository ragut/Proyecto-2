import base64
from ..controller.DatabasesController import DatabasesController

class User():

    id = None
    names = None
    lastnames = None
    email = None
    password = None

    database = DatabasesController()

    def __init__(self):
        self.id = None
        self.names = None
        self.lastnames = None
        self.email = None
        self.password = None

    def set_variables_user(self, names, lastnames, email, password):
        self.id = None
        self.names = names
        self.lastnames = lastnames
        self.email = email
        self.password = base64.b64encode(password)
        #self.password = password

    def set_variables_db(self, dictionary):
        self.id = str(dictionary["_id"])
        self.names = dictionary["names"]
        self.lastnames = dictionary["lastnames"]
        if "email" in dictionary:
            if dictionary["email"] is None:
                self.email = None
            else:
                self.email = dictionary["email"]
        else:
            self.email = None

        if "password" in dictionary:
            if dictionary["password"] is None:
                self.password = None
            else:
                self.password = dictionary["password"]
        else:
            self.password = None

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id),"names":self.names , "lastnames": self.lastnames, "email": self.email, "password": self.password}

    def to_save(self):
        return {"names":self.names , "lastnames": self.lastnames, "email": self.email, "password": self.password}