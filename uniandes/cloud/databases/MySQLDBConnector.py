import os
import datetime
import peewee as pw
import random
db = pw.MySQLDatabase(os.environ["database_name"],
                      host=os.environ["database_host"],
                      port=int(os.environ["database_port"]),
                      user=os.environ["database_user"],
                      passwd=os.environ["database_pwd"])

class BaseModel(pw.Model):
    class Meta:
        database = db

class User(BaseModel):
    id = pw.PrimaryKeyField(unique=True)
    names = pw.TextField()
    lastnames = pw.TextField()
    email = pw.TextField()
    password = pw.TextField()


    def to_dictionary(self):
        return {"_id":self.id, "names": self.names, "lastnames": self.lastnames, "email":self.email,
                "password": self.password}

    def to_save_dictionary(self):
        return {"_id":self.id, "names": self.names, "lastnames": self.lastnames, "email":self.email,
                "password": self.password}

class Contest(BaseModel):
    id = pw.PrimaryKeyField(unique=True)
    user_id = pw.ForeignKeyField(User)
    names = pw.TextField()
    url = pw.TextField()
    baner = pw.TextField()
    date_ini = pw.DateTimeField()
    deadline = pw.DateTimeField()
    description = pw.TextField()


    def to_dictionary(self):
        return {"_id":self.id, "user_id": self.user_id.id, "name": self.names, "url":self.url,
                "baner": self.baner, "date_ini": self.date_ini, "deadline": self.deadline, "description": self.description}

class Video(BaseModel):
    id = pw.PrimaryKeyField(unique=True)
    user_id = pw.ForeignKeyField(User)
    contest_id = pw.ForeignKeyField(Contest)
    video_name = pw.TextField()
    email = pw.TextField()
    names_user = pw.TextField()
    lastnames_user = pw.TextField()
    date = pw.DateTimeField()
    status = pw.TextField()
    original_file = pw.TextField()


    def to_dictionary(self):
        return {"_id":self.id, "user_id": self.user_id.id, "contest_id": self.contest_id.id, "video_name":self.video_name,
                "email": self.email, "names_user": self.names_user, "lastnames_user": self.lastnames_user, "date": self.date.strftime("%Y/%m/%d - %H:%M:%S"),
                "status": self.status, "original_file": self.original_file }


class MySQLDBConnector():
    def __init__(self):
        db.connect()
        db.create_tables([User, Contest, Video], safe=True)

    def createUser(self, user):
        if User.select().where(User.email == user.email).count() == 0:
            inserted = User.create(names = user.names,
                                   lastnames = user.lastnames,
                                   email = user.email,
                                   password = user.password)
            user.set_id(inserted.id)
            db.close()
            return user
        else:
            db.close()
            return None


    def user_url_exist(self, url):
        if Contest.select().where(Contest.url == url).count() == 0:
            db.close()
            return False
        else:
            db.close()
            return True

    def getUsers(self):
        users = []
        for user in User.select().order_by(User.id.desc()):
            users.append(user.to_save_dictionary())
        db.close()
        return users

    def getUser(self, id):
        try:
            user = User.get(User.id == int(id))
            db.close()
            return user.to_save_dictionary()
        except:
            db.close()
            return None

    def getUserByUrl(self, url):
        try:
            user = User.get(User.url == url)
            db.close()
            return user.to_save_dictionary()
        except:
            db.close()
            return None

    def updateCompanyUser(self, user):
        user = User(id = user.id,
                    names = user.names,
                    lastnames = user.lastnames,
                    email = user.email,
                    password = user.password)
        user.save()
        db.close()
        return user.to_dictionary()

    def deleteUser(self, id):
        try:
            user = User.get(User.id == int(id))
            user.delete_instance()
            db.close()
            return True
        except:
            db.close()
            return False

    def confirmLogin(self, email, password):
        try:
            user = User.get((User.email == email) & (User.password == password))
            db.close()
            return user.to_save_dictionary()
        except:
            db.close()
            return None

    def getLatestUser(self):
        users = []
        for user in User.select().order_by(User.id.desc()).limit(6):
            users.append(user.to_save_dictionary())
        db.close()
        return users

    def getLatestVideo(self):
        videos = []
        for video in Video.select().where(Video.status == "OK").order_by(Video.date.desc()).limit(10):
            videos.append(video.to_dictionary())
        db.close()
        return videos

    def createContest(self, contest):
        if Contest.select().where(Contest.url == contest.url).count() > 0:
            url_nueva = contest.url+"_"+contest.user_id+"_"+str(random.randrange(1, 101, 2))
            contest.url = url_nueva

        inserted = Contest.create(user_id_id = contest.user_id,
                        names = contest.names,
                        url = contest.url,
                        baner = contest.banner,
                        date_ini = contest.date_ini,
                        deadline = contest.deadline,
                        description = contest.description)
        contest.set_id(inserted.id)
        db.close()
        return contest


    def getUserContest(self, contest_id):
        contests = []
        cp_prj = Contest.select().where(Contest.user_id_id == int(contest_id)).order_by(Contest.id.desc())
        for contest in cp_prj:
            contests.append(contest.to_dictionary())
        db.close()
        return contests

    def getContest(self, id):
        try:
            contest = Contest.get(Contest.id == int(id))
            db.close()
            return contest.to_dictionary()
        except:
            db.close()
            return None

    def getContestAll(self):
        contests = []
        for contest in Contest.select().order_by(Contest.id.desc()):
            contests.append(contest.to_dictionary())
        db.close()
        return contests

    def getURLContest(self, url):
        try:
            contest = Contest.get(Contest.url == url)
            db.close()
            return contest.to_dictionary()
        except:
            db.close()
            return None

    def updateContest(self, contest):
        contest = Contest(id=contest.id,
                           user_id_id = contest.user_id,
                            names = contest.names,
                            baner = contest.banner,
                            date_ini = contest.date_ini,
                            deadline = contest.deadline,
                            description = contest.description)
        contest.save()
        db.close()
        return contest

    def updateContestBanner(self, contest):
        contest = Contest(id=contest.id,
                           user_id_id = contest.user_id,
                            names = contest.names,
                            date_ini = contest.date_ini,
                            deadline = contest.deadline,
                            description = contest.description)
        contest.save()
        db.close()
        return contest

    def deleteContest(self, id):
        try:
            contest = Contest.get(Contest.id == int(id))
            contest.delete_instance()
            db.close()
            return True
        except:
            db.close()
            return False

    def getUserContestNumber(self, user_id):    #//OK
        try:
            number = Contest.select().where(Contest.user_id == int(user_id)).count()
            db.close()
            return number
        except:
            db.close()
            return -1

    def getContestVideoNumber(self, contest_id):        #//OK
        try:
            number = Video.select().where(Video.contest_id == int(contest_id)).count()
            db.close()
            return number
        except:
            db.close()
            return -1

    def getUserVideoNumber(self, user_id):
        try:
            number = Video.select().where(Video.user_id == int(user_id)).count()
            db.close()
            return number
        except:
            db.close()
            return -1

    def createVideo(self, video):
        inserted = Video.create(user_id = video.user_id,
                                contest_id = video.contest_id,
                                video_name  = video.video_name,
                                email = video.email,
                                names_user = video.names_user,
                                lastnames_user = video.lastnames_user,
                                status = video.status,
                                original_file = video.original_file,
                                date = datetime.datetime.strptime(video.date, "%Y/%m/%d - %H:%M:%S"))

        video.set_id = inserted.id
        db.close()
        return video

#//----  OBTIENE LISTA DE VIDEOS ----//
    def getContestOkVideos(self, contest_id):
        videos = []
        for video in Video.select().where((Video.contest_id == int(contest_id)) & (Video.status == "OK")).order_by(Video.date.desc()):
            videos.append(video.to_dictionary())
        db.close()
        return videos

    def getContestVideo(self, contest_id):
        videos = []
        for video in Video.select().where(Video.contest_id == int(contest_id)).order_by(Video.date.desc()):
            videos.append(video.to_dictionary())
        db.close()
        return videos

    def getVideo(self):
        videos = []
        for video in Video.select().sort(Video.date.desc()):
            videos.append(video.to_dictionary())
        db.close()
        return videos

    def getOkVideos(self):
        videos = []
        for video in Video.select().where(Video.status == "OK").order_by(Video.date.desc()):
            videos.append(video.to_dictionary())
        db.close()
        return videos

    def video_file_name_exist(self, file_name):
        if Video.select().where(Video.file_name == file_name).count() == 0:
            db.close()
            return False
        else:
            db.close()
            return True

    def getProcessVideo(self):
        videos = []
        for video in Video.select().where(Video.status == "On Process").order_by(Video.date.desc()):
            videos.append(video.to_dictionary())
        db.close()
        return videos

#//----     VIDEOS PARA PROCESAR    ----//
    def getVideoToProcess(self):
        try:
            video = Video.select().where(Video.status == "On Process").order_by(Video.date.desc()).limit(1).first()
            video.status = "Processing"
            video.save()
            db.close()
            return video.to_dictionary()
        except:
            db.close()
            return None

    def updateStatusVideo(self, video_id):
        video = Video.get(Video.id == int(video_id))
        video.status = "OK"
        video.save()
        db.close()
        return video.to_dictionary()

    def deleteVideo(self, id):
        try:
            video = Video.get(Video.id == int(id))
            video.delete_instance()
            db.close()
            return True
        except:
            db.close()
            return False