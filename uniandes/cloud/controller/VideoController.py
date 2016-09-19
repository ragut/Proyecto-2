import os

from .DatabasesController import DatabasesController
from ..model.ContestVideo import ContestVideo
from .FileController import FileController

class VideoController():

    database = None
    fileSystem = None

    def __init__(self):
        self.database = DatabasesController()
        self.fileSystem = FileController()

#//----     CREA EL VIDEO   -----//
    def createVideo(self, user_id, contest_id, name_video, email, names_user, lastnames_user, videoFile, extension):
        video = ContestVideo()
        video.set_variables_video(user_id,contest_id, name_video, email, names_user, lastnames_user, "On Process", extension)
        self.fileSystem.save_original_video(videoFile, video.video_name, video.original_file)
        return self.database.createVideo(video)


#//----  OBTIENE LOS VIDEOS PROCESADOS DEL CONCURSO   ----//
    def getContestOkVideos(self, contest_id):
        data = self.database.getContestOkVideos(contest_id)
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----     TRAE LOS VIEDOS ----//
    def getContestVideo(self, contest_id):
        data = self.database.getContestVideo(contest_id)
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//-----    PROCESA LOS VIDEOS  ----//
    def getProcessVideo(self):
        data = self.database.getProcessVideo()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//---- ACTUALIZA EL ESTADO DEL VIDEO   ----//
    def updateStatusVideo(self, video_id):
        return self.database.updateStatusVideo(video_id)

#//---- OBTIENE LOS VIDEOS PARA PROCESAR   ----//
    def getVideoToProcess(self):
        video = self.database.getVideoToProcess()
        if video is not None:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            return tmp_video
        else:
            return None

#//----     TRAE LOS ULTIMOS 10 VIDEOS   ----//
    def getLatestVideo(self):
        data = self.database.getLatestVideo()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----     ACTUALIZA EL ESTADO DEL VIDEO   ----//
    def getOkVideos(self):
        data = self.database.getOkVideos()
        videos = []
        for video in data:
            tmp_video = ContestVideo()
            tmp_video.set_variables_db(video)
            videos.append(tmp_video)
        return videos

#//----      ELIMINA VIDEO   ----//
    def deleteContestVideo(self, contest_id):       #//OK
        videos = self.getContestVideo(contest_id)
        for video in videos:
            self.fileSystem.delete_video(video)
            self.database.deleteVideo(video.id)
        return True