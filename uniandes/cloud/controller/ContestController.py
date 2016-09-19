from ..model.Contest import Contest
from .VideoController import VideoController
from .DatabasesController import DatabasesController
from .ImageService import ImageService
from .FileController import FileController

class ContestController():

    database = None
    fileSystem = None

    def __init__(self):
        self.database = DatabasesController()
        self.fileSystem = FileController()

#//---- INSERTA CONCURSO    -----//
    def insertContest(self, user_id, names, date_ini, deadline, description, url, baner):
        contest = Contest()
        contest.set_variables_contest(user_id, names, date_ini, deadline, description, url)
        img = ImageService().generate_img(baner)
        self.fileSystem.save_contest_banner(img, contest.banner)

        return self.database.createContest(contest)

#//---- OBTIENE CONCURSOS POR USUARIO   ----//
    def getUserContest(self, user_id):
        data = self.database.getUserContest(user_id)
        contests = []
        for contest in data:
            newContest = Contest()
            newContest.set_variables_db(contest)
            contests.append(newContest)
        return contests

#//-----    OBTIENE CONCURSO ESPECIFICO ----//
    def getContest(self, contest_id):
        data = self.database.getContest(contest_id)
        contest = Contest()
        contest.set_variables_db(data)
        return contest

    def getContestAll(self):
        data = self.database.getContestAll()
        contest = Contest()
        contest.set_variables_db_2(data)
        return contest

    #//-----    OBTIENE CONCURSO ESPECIFICO ----//
    def getURLContest(self, contest_url):
        data = self.database.getURLContest(contest_url)
        contest = Contest()
        contest.set_variables_db(data)
        return contest

#//-----    ACTUALIZA CONCURSO ESPECIFICO ----//
    def updateContest(self, id, user_id,  name, date_ini, deadline, description, url, baner):
        contest = Contest()
        contest.set_variables_contest(user_id,  name, date_ini, deadline, description, url)
        contest.set_id(id)

        img = ImageService().generate_img(baner)
        self.fileSystem.save_contest_banner(img, contest.banner)

        return self.database.updateContest(contest)

#//-----    ELIMINA CONCURSO ESPECIFICO ----//
    def deleteContest(self, id):
        VideoController().deleteContestVideo(id)
        return self.database.deleteContest(id)

