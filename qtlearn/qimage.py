__author__ = 'g7842'

from PyQt4 import QtCore, QtGui


class ImageButton(QtGui.QLabel):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.SubWindow | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _setNewImage(self, image):
        self.setPixmap(QtGui.QPixmap(image))

    def loadFromUrl(self, url):
        result = False

        import urllib2
        try:
            # Wikipedia require any header
            # req = urllib.request.Request(url,
            #                         headers={'User-Agent': version.AppName})
            # data = urllib.request.urlopen(req).read()
            image = QtGui.QImage()
            result = image.loadFromData(urllib2.urlopen(url, timeout=3).read())
            if result:
                self._setNewImage(image)
        except:
            pass
        return result

    def loadFromUrlByQFile(self, url):
        file = QtCore.QFile()
        file.open()

        file = QtCore.QFile(url)
        if not file.open(QtCore.QIODevice.WriteOnly):
            return False
        file.write(data.readAll())
        file.close()

    def paintEvent(self, QPaintEvent):
        print('abc')


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    wnd = ImageButton()
    wnd.loadFromUrl("http://p0.qhimg.com/t0185a14f94ff6aea0a.jpg")
    # wnd.setText('BUTTON')
    wnd.show()
    sys.exit(app.exec_())