__author__ = 'g7842'

import sys
from PyQt4 import QtGui,QtCore

def main1():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250, 250)
    w.move(300, 300)
    w.setWindowTitle('simple')
    w.show()

    #The mainloop ends if we call the exit() method or the main widget is destroyed. The sys.exit()
    sys.exit(app.exec_())


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        #QtGui.QWidget.__init__(None)
        self.initUI()
        self.center()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        #close
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('C:/Users/G7842/PycharmProjects/Learn/test.jpg'))
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main2():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # main1()
    main2()
