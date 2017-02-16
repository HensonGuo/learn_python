__author__ = 'g7842'

# In the event model, there are three participants:
#
# event source
# event object
# event target

import sys
from PyQt4 import QtGui, QtCore


class SignalSlotsExample(QtGui.QWidget):

    def __init__(self):
        super(SignalSlotsExample, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Backspace:
            self.close()


class EventSenderExample(QtGui.QMainWindow):
    closeApp = QtCore.pyqtSignal()

    def __init__(self):
        super(EventSenderExample, self).__init__()
        self.initUI()

    def initUI(self):
        self.closeApp.connect(self.close)

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def mousePressEvent(self, *args, **kwargs):
        self.closeApp.emit()

def main1():
    app1 = QtGui.QApplication(sys.argv)
    ss = EventSenderExample()
    sys.exit(app1.exec_())

if __name__ == '__main__':
    main1()