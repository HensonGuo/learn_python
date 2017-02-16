# coding=utf-8
__author__ = 'g7842'


from PyQt4 import QtCore, QtGui


#文件的读写、数据的请求等待、图片下载等异步操作都可以使用多线程，不影响界面
class RunnableQObject(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(RunnableQObject, self).__init__(parent)

    def callFinished(self):
        self.finished.emit()

    def run(self):
        pass


class Runnable(QtCore.QRunnable):
    def __init__(self, runnableQObject=None):
        super(Runnable, self).__init__()
        self.runnableQObject = runnableQObject

    def run(self):
        if self.runnableQObject:
            self.runnableQObject.run()
            self.runnableQObject.callFinished()


class XThreadPool(QtCore.QThreadPool):
    def __init__(self, parent=None):
        super(XThreadPool, self).__init__(parent)

    def startRunnableQObject(self, runnableQObject, priority=0):
        runnable = Runnable(runnableQObject)
        self.start(runnable, priority)

    _shareInstance = None
    @staticmethod
    def shareInstance(parent=None):
        if not XThreadPool._shareInstance:
            XThreadPool._shareInstance = XThreadPool(parent)
            XThreadPool._shareInstance.setMaxThreadCount(60)
        return XThreadPool._shareInstance



if "__main__" == __name__:
    class AddObject(RunnableQObject):
        finishedData = QtCore.pyqtSignal(int)
        def __init__(self, maxValue=10000, parent=None):
            super(AddObject, self).__init__(parent)
            self.maxValue = maxValue
            self.i = 1

        def callFinished(self):
            super(AddObject, self).callFinished()

        def run(self):
            while self.i < self.maxValue:
                self.i += 1
            print "threadId:", int(QtCore.QThread.currentThreadId())
            print "result:", self.i

    class Result(QtCore.QObject):
        def __init__(self, parent=None):
            super(Result, self).__init__(parent)

        def printResult(self):
            print "value:"
            print ""

    import sys
    app = QtGui.QApplication(sys.argv)
    resultObject = Result()

    addObject = AddObject(1234500)
    addObject.finished.connect(resultObject.printResult)
    XThreadPool.shareInstance().startRunnableQObject(addObject)

    addObject1 = AddObject(5432100)
    addObject1.finished.connect(resultObject.printResult)
    XThreadPool.shareInstance().startRunnableQObject(addObject1)

    addObject2 = AddObject(9999900)
    addObject2.finished.connect(resultObject.printResult)
    XThreadPool.shareInstance().startRunnableQObject(addObject2)

    app.exec_()
