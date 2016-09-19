import unicodedata
import random
from ..controller.DatabasesController import DatabasesController

#//----- MODELO DEL CONCURSO -----//
class Contest():

    id = None
    user_id = None
    name = None
    banner = None
    url = None
    date_ini = None
    deadline = None
    description = None
    num_video = -1

    database = DatabasesController()

    def __init__(self):
        self.id = None
        self.user_id = None
        self.names = None
        self.banner = None
        self.url = None
        self.date_ini = None
        self.deadline = None
        self.description = None

        self.num_video = -1

#//-----    FUNCIONES CRUD MODELO CONCURSO    -----//

    def set_num_video(self, num_video):
        self.num_video = num_video

    def set_variables_contest(self, user_id, name, date_ini, deadline, description, url):
        self.id = None
        self.user_id = str(user_id)
        self.names = name
        self.url = url
        self.generate_url()
        self.banner = self.url+".png"
        self.date_ini = date_ini
        self.deadline = deadline
        self.description = description


    def set_variables_db(self, dictionary):
        self.id = str(dictionary["_id"])
        self.user_id = str(dictionary["user_id"])
        self.names = dictionary["name"]
        self.banner = dictionary["baner"]
        self.url = dictionary["url"]
        self.date_ini = dictionary["date_ini"]
        self.deadline = dictionary["deadline"]
        self.description = dictionary["description"]


    def generate_url(self):
        if self.url is not None:
            url_aux = unicodedata.normalize('NFKD', self.url).encode('ASCII', 'ignore')
            url_aux = url_aux.lower()
            url_aux = url_aux.replace(" ","_")

            final_url = url_aux
            exist = self.database.user_url_exist(final_url)

            while exist == True:
                final_url = url_aux + "_" + str(random.randrange(1, 101, 2))
                exist = self.database.user_url_exist(final_url)

            self.url = final_url

    def set_id(self, id):
        self.id = str(id)

    def to_dict(self):
        return {"_id":str(self.id), "user_id":self.user_id, "name": self.name, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}

    def to_save(self):
        return {"user_id":self.user_id, "name": self.name, "banner": self.banner,
                "url": self.url, "date_ini":self.date_ini, "deadline":self.deadline, "description":self.description}