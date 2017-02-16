__author__ = 'g7842'

from PyQt4 import QtCore

def formatTimeToStr(time):
    time = QtCore.QDateTime.fromString(time, "yyyy-MM-dd hh:mm:ss")
    return time.toString("yyyy-MM-dd")