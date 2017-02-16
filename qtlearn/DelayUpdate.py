__author__ = 'g7842'

from PyQt4 import QtCore

class DelayUpdate(QtCore.QObject):
    base = 10

    def __init__(self):
        super(DelayUpdate, self).__init__()
        self._timer = QtCore.QTimer(self)
        self._timer.setInterval(DelayUpdate.base)
        self._timer.timeout.connect(self._onExcute)
        self._calls = []
        self._index = 0

    @staticmethod
    def instance():
        """
        :rtype : DelayUpdate
        """
        if DelayUpdate._instance is None:
            print DelayUpdate.print_stack()
        return DelayUpdate._instance

    _instance = None
    @staticmethod
    def initInstance():
        if DelayUpdate._instance is not None:
            DelayUpdate._instance.release()
        DelayUpdate._instance = DelayUpdate()
        return DelayUpdate._instance

    def delayExcute(self, func, data, delay):
        if delay % DelayUpdate.base != 0:
            raise ValueError('delay value error')
        self._calls.append({'func':func, 'data':data, 'delay':delay, 'index':self._index})
        if not self._timer.isActive():
            self._timer.start()

    def clear(self):
        self._calls = []
        if self._timer.isActive():
            self._timer.stop()

    def _onExcute(self):
        self._index += 1
        for i in range(0, 10):
            if not len(self._calls):
                self._timer.stop()
                self._index = 0
                return
            i = 0
            for call in self._calls:
                delay = call['delay']
                index = call['index']
                passTime = (self._index - index) * DelayUpdate.base
                if passTime % delay == 0:
                    func = call['func']
                    data = call['data']
                    func(data)
                    self._calls.pop(i)
                    i += 1
                    break



