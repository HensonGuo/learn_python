__author__ = 'g7842'

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_resource(object):
    def setupUi(self, resource):
        resource.setObjectName(_fromUtf8("main"))
        resource.resize(400, 300)

        self.retranslateUi(resource)
        QtCore.QMetaObject.connectSlotsByName(resource)

    def retranslateUi(self, resource):
        resource.setWindowTitle(_translate("main", "Form", None))


class showresource(QtGui.QWidget):
    def __init__(self):
        super(showresource, self).__init__()

        palette1 = QtGui.QPalette(self)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(':/imgs/header_bg.png')))

        self.setPalette(palette1)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


import sys
if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv)
     resource = showresource()
     resource.show()
     sys.exit(app.exec_())