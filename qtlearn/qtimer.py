__author__ = 'g7842'

from PyQt4 import QtCore, QtGui
import sys

class Test(QtGui.QWidget):
    def __init__(self):
        super(Test, self).__init__()
        QtCore.QTimer.singleShot(2000, self.printtt)

    def printtt(self):
        print('nima')


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()