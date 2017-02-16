__author__ = 'g7842'

from PyQt4 import QtCore, QtNetwork
from ThreadPool import XThreadPool, RunnableQObject
import os, traceback

class SaveFileTask(RunnableQObject):
    saveFileFinished = QtCore.pyqtSignal(int, str, str)
    def __init__(self, filePath, fileData, urlStr, parent=None):
        super(SaveFileTask, self).__init__(parent)
        self.urlStr = urlStr
        self.filePath = filePath
        self.fileData = fileData

    def run(self):
        file = QtCore.QFile(self.filePath)
        if not file.open(QtCore.QIODevice.WriteOnly):
            self.saveFileFinished.emit(SAVE_FILE_ERROR, self.urlStr, self.filePath)
        file.write(self.fileData)
        file.close()
        self.saveFileFinished.emit(0, self.urlStr, self.filePath)

SAVE_FILE_ERROR = 999

class DownloadManager(QtCore.QObject):
    downloadFinished = QtCore.pyqtSignal(int, str, str)

    def __init__(self, path=None, parent=None):
        super(DownloadManager, self).__init__(parent)
        self.networkMgr = QtNetwork.QNetworkAccessManager(self)
        self.networkMgr.finished.connect(self._onDownloadFinished)
        self.storagePath = None
        self.isDelSuffix = False

        if path:
            self.setStoragePath(path)
            if not os.path.exists(self.getStoragePath()):
                os.makedirs(self.getStoragePath())

    @staticmethod
    def instance():
        """
        :rtype : DownloadManager
        """
        if DownloadManager._instance is None:
            print traceback.print_stack()
        return DownloadManager._instance

    _instance = None
    @staticmethod
    def initInstance(path):
        if DownloadManager._instance is not None:
            DownloadManager._instance.release()
        DownloadManager._instance = DownloadManager(path)
        return DownloadManager._instance

    def download(self, url, forceDownload=False):
        qUrl = QtCore.QUrl(url)
        if not qUrl.isValid():
            self.downloadFinished.emit(QtNetwork.QNetworkReply.HostNotFoundError, qUrl.toString(), "")
            return ""

        if self.storagePath and self.isFileExist(qUrl) and not forceDownload:
            return self.getFilePath(qUrl)
        else:
            request = QtNetwork.QNetworkRequest(qUrl)
            reply = self.networkMgr.get(request)
            return ""

    def _onDownloadFinished(self, reply):
        qUrl = reply.url()
        if reply.error():
            self.downloadFinished.emit(reply.error(), qUrl.toString(), self.getFilePath(qUrl))
        else:
            if self.storagePath:
                self.postSaveFileTask(reply)
            else:
                self.downloadFinished.emit(0, qUrl.toString(), qUrl.path())
        reply.deleteLater()

    def delFuffix(self):
        self.isDelSuffix = True

    def getFileName(self, qUrl):
        path = qUrl.path()
        if self.isDelSuffix:
            path = path.split('.')[0]
        basename = QtCore.QFileInfo(path).fileName()
        return basename

    def getFilePath(self, qUrl):
        return self.storagePath + self.getFileName(qUrl)

    def isFileExist(self, qUrl):
        if QtCore.QFile.exists(self.getFilePath(qUrl)):
            return True
        return False

    def getStoragePath(self):
        return self.storagePath

    def setStoragePath(self, path):
        self.storagePath = path

    def saveFile(self, fileName, data):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QIODevice.WriteOnly):
            return False
        file.write(data.readAll())
        file.close()
        return True

    def postSaveFileTask(self, reply):
        filePath = self.getFilePath(reply.url())
        if self.isDelSuffix:
            filePath = filePath.split('.')[0]

        fileData = reply.readAll()
        urlStr = reply.url().toString()
        saveFileTask = SaveFileTask(filePath, fileData, urlStr)
        saveFileTask.saveFileFinished.connect(self.downloadFinished)
        XThreadPool.shareInstance().startRunnableQObject(saveFileTask)
