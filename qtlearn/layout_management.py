__author__ = 'g7842'

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        #GridLayout
        # grid = QtGui.QGridLayout()
        # self.setLayout(grid)
        #
        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #         '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #         '0', '.', '=', '+']
        # positons = [(i,j) for i in range(5) for j in range(4)]
        #
        # for positon, name in zip(positons, names):
        #     if name == '':
        #         continue
        #     button = QtGui.QPushButton(name)
        #     grid.addWidget(button, *positon)



        #Box Layout
        okButton = QtGui.QPushButton('OK')
        okButton.setGeometry(0, 0, 100, 200)
        # okButton.setFixedSize(100, 200)
        cancelButton = QtGui.QPushButton('CANCEL')

        # hbox = QtGui.QHBoxLayout(self)
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(vbox)
        vbox.addWidget(okButton)
        vbox.addWidget(cancelButton)

        self.setLayout(vbox)

        #Absolute
        # lbl1 = QtGui.QLabel('Zetcode', self)
        # lbl1.move(15, 10)
        # lbl2 = QtGui.QLabel('tutorials', self)
        # lbl2.move(35, 40)
        # lbl3 = QtGui.QLabel('for programmers', self)
        # lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


class Review(QtGui.QWidget):
    def __init__(self):
        super(Review, self).__init__()
        self.initUI()

    def initUI(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('author')
        review = QtGui.QLabel('review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    # re = Review()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()