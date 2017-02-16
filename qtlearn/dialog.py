__author__ = 'g7842'

import sys
from PyQt4 import QtGui

class InputDialogExample(QtGui.QWidget):

    def __init__(self):
        super(InputDialogExample, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit()
        self.le.move(130, 22)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setPixmap(QtGui.QPixmap('_files/min.png'))

        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))


class ColorExample(QtGui.QWidget):

    def __init__(self):
        super(ColorExample, self).__init__()

        self.initUI()

    def initUI(self):

        col = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):

        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


class QFontDialog(QtGui.QWidget):

    def __init__(self):
        super(QFontDialog, self).__init__()

        self.initUI()

    def initUI(self):

        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton('Dialog', self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

class QFileDialog(QtGui.QMainWindow):

    def __init__(self):
        super(QFileDialog, self).__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = InputDialogExample()
    # ex = ColorExample()
    # ex = QFontDialog()
    # ex = QFileDialog()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()