from ..databases.MySQLDBConnector import MySQLDBConnector


class DatabasesController():
    database = None

    def __init__(self):
        self.database = MySQLDBConnector()

    def createUser(self, user):
        return self.database.createUser(user)

    def user_url_exist(self, url):
        return self.database.user_url_exist(url)

    def getUsers(self):      #OK
        return self.database.getUsers()

    def getUser(self, id):      #OK
        return self.database.getUser(id)

    def getUserByUrl(self, url):        #OK
        return self.database.getUserByUrl(url)

    def updateUser(self, user):
        return self.database.getUserByUrl(user)

    def deleteUser(self, id):           #OK
        return self.database.deleteUser(id)

    def confirmLogin(self, email, password):        #OK
        return self.database.confirmLogin(email, password)

    def createContest(self, contest):               #//OK
        return self.database.createContest(contest)

    def getUserContest(self, user_id):              #//OK
        return self.database.getUserContest(user_id)

    def getContest(self, id):                       #//OK
        return self.database.getContest(id)

    def getContestAll(self):                       #//OK
        return self.database.getContestAll()

    def getURLContest(self, url):                       #//OK
        return self.database.getURLContest(url)

    def updateContest(self, contest):               #//OK
        return self.database.updateContest(contest)

    def updateContestBanner(self, contest):               #//OK
        return self.database.updateContestBanner(contest)

    def deleteContest(self, id):                    #//OK
        return self.database.deleteContest(id)

    def getUserContestNumber(self, user_id):           #//OK
        return self.database.getUserContestNumber(user_id)

    def getContestVideoNumber(self, contest_id):              #//OK
        return self.database.getContestVideoNumber(contest_id)

    def getUserVideoNumber(self, company_id):               #//OK
        return self.database.getUserVideoNumber(company_id)

    def createVideo(self, video):                   #//OK
        return self.database.createVideo(video)

    def getContestOkVideos(self, contest_id):           #//OK
        return self.database.getContestOkVideos(contest_id)

    def getContestVideo(self, project_id):          #//OK
        return self.database.getContestVideo(project_id)

    def getVideo(self):             #//OK
        return self.database.getVideo()

    def getOkVideos(self):          #//OK
        return self.database.getOkVideos()

    def video_file_name_exist(self, file_name): #OK
        return self.database.video_file_name_exist(file_name)

    def getProcessVideo(self):      #OK
        return self.database.getProcessVideo()

    def updateStatusVideo(self, video_id):  #OK
        return self.database.updateStatusVideo(video_id)

    def deleteVideo(self, id):  #OK
        return self.database.deleteVideo(id)

    def getLatestUser(self):        #OK
        return self.database.getLatestUser()

    def getLatestVideo(self):       #OK
        return self.database.getLatestVideo()

    def getVideoToProcess(self):        #OK
        return self.database.getVideoToProcess()