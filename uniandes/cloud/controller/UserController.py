import base64

from ..model.User import User
from .ImageService import ImageService
from .DatabasesController import DatabasesController
from .FileController import FileController

class UserController():

    database = None
    fileSystem = None

    def __init__(self):
        self.database = DatabasesController()
        self.fileSystem = FileController()

    def add_User(self, names, lastnames, email, password):
        user = User()
        user.set_variables_user(names, lastnames, email, password)
        data = self.database.createUser(user)

        if data is None:
            return None
        else:
            data.email = None
            data.password = None
            return data

    def login_user(self, email, password):
        data = self.database.confirmLogin(email, base64.b64encode(password))
        #data = self.database.confirmLogin(email, password)
        user = None
        if data is not None:
            user = User()
            user.set_variables_db(data)
        return user

    def getUserFromDict(self, dictionary):
        user = User()
        user.set_variables_db(dictionary)
        return user

    def getUserFromUrl(self, url):
        data = self.database.getUserByUrl(url)
        tmp_user = None
        if data is not None:
            tmp_user = User()
            tmp_user.set_variables_db(data)
        return tmp_user

    def getUserContestNumber(self, user_id):
        return self.database.getUserContestNumber(user_id)

    def getUserVideoNumber(self, user_id):
        return self.database.getUserVideoNumber(user_id)

    def getUserId(self, user_id):
        data = self.database.getUser(user_id)
        tmp_user = None
        if data is not None:
            tmp_user = User()
            tmp_user.set_variables_db(data)
        return tmp_user

    def getLatestUser(self):
        users = []
        for user in self.database.getLatestUser():
            tmp_user = User()
            tmp_user.set_variables_db(user)
            users.append(tmp_user)
        return users

    def getUsers(self):
        users = []
        for user in self.database.getUsers():
            tmp_user = User()
            tmp_user.set_variables_db(user)
            users.append(tmp_user)
        return users