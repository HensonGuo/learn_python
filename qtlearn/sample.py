# coding=utf-8
__author__ = 'g7842'


from PyQt4 import QtGui, QtCore
from Download import DownloadManager
from DelayUpdate import DelayUpdate

class SampleWgt(QtGui.QMainWindow):
    ignore_star = QtCore.pyqtSignal(str, str)
    MaxColumn = 4
    MaxRaw = 600

    def __init__(self):
        super(SampleWgt, self).__init__()
        self.setFixedSize(955, 900)
        self._selectedTag = '*'
        self._sortName = None
        self._conf = None
        self._downloadMgr = DownloadManager.initInstance('file/img/')
        self._downloadMgr.delFuffix()
        DelayUpdate.initInstance()
        self._tagSort = False
        self.genres = None
        self._initUI()
        self._selectedClass = '*'
        self._data = {}
        for i in xrange(600):
            id = i % 2
            if id == 0:
                image = 'http://cdn.duitang.com/uploads/item/201407/01/20140701151513_LFPmU.jpeg'
                name = u'汪汪'
            else:
                image = 'http://cdnq.duitang.com/uploads/item/201507/14/20150714071144_txJ43.thumb.700_0.jpeg'
                name = u'喵喵'
            dta = {'image':image, 'text':'', 'id':id, 'name':name}
            self._data[i] = dta
        self.selectTag('*')

    def _initUI(self):
        self._table = QtGui.QTableWidget(self)
        self._table.verticalHeader().setVisible(False)
        self._table.horizontalHeader().setVisible(False)
        self._table.setColumnCount(SampleWgt.MaxColumn)
        self._table.setRowCount(SampleWgt.MaxRaw)
        self._table.setGeometry(5, 5, 825, self.height() - 30)
        self._itemPool = []

        self._opArea = QtGui.QWidget(self)
        self._opArea.setGeometry(self._table.width() + 20, 20, 200, 300)

        self._btnGroup = QtGui.QButtonGroup()
        self._btnGroup.buttonClicked.connect(lambda :self.selectTag(self._btnGroup.checkedButton().text()))

        self._lyt = QtGui.QVBoxLayout()
        self._lyt.setContentsMargins(0, 0, 0, 0)
        self._lyt.setSpacing(0)
        self._lyt.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self._opArea.setLayout(self._lyt)
        i= 0
        clses = ['*', u'喵星人', u'汪星人']
        for cls in clses:
            cb = QtGui.QCheckBox()
            cb.setFixedSize(80, 20)
            cb.setText(cls)
            cb.setCheckable(True)
            if cls == '*':
                cb.setChecked(True)
            i+=1
            self._lyt.addWidget(cb)
            self._btnGroup.addButton(cb)
            self._btnGroup.setId(cb, i)

    def selectTag(self, tag):
        self._selectedTag = unicode(tag)
        self.update()

    def update(self):
        self._table.clear()
        filtereds = []
        for key in self._data:
            animal = self._data[key]
            id = animal.get('id', 0)
            if self._selectedTag == '*':
                filtereds.append(animal)
            elif self._selectedTag == u'喵星人' and id == 1:
                filtereds.append(animal)
            elif self._selectedTag == u'汪星人' and id == 0:
                filtereds.append(animal)

        DelayUpdate.instance().clear()

        raw = 0
        count = 0
        for i in range(0, filtereds.__len__()):
            animal = filtereds[i]
            count += 1
            if count > SampleWgt.MaxColumn:
                raw += 1
                count = 1
            DelayUpdate.instance().delayExcute(self._addItem, {'animal':animal, 'raw':raw, 'column':count - 1}, 20)
            # self._addItem({'animal':animal, 'raw':raw, 'column':count - 1})

        for i in range(raw + 1, SampleWgt.MaxRaw):
            self._table.setRowHidden(i, True)
        self._table.resizeRowsToContents()
        self._table.resizeColumnsToContents()

    def _addItem(self, data):
        animal = data['animal']
        raw = data['raw']
        column = data['column']

        if self._itemPool.__len__() > 0:
            wgt = self._itemPool.pop(0)
        else:
            wgt = ItemWgt()
            wgt.setDownloadMgr(self._downloadMgr)
            wgt.installEventFilter(self)
        wgt.updateInfo(animal)
        if self._table.isRowHidden(raw):
            self._table.setRowHidden(raw, False)
        self._table.setCellWidget(raw, column, wgt)
        self._table.resizeRowsToContents()
        self._table.resizeColumnsToContents()


class ItemWgt(QtGui.QWidget):
    dataChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ItemWgt, self).__init__(parent)
        self.setFixedSize(200, 320)

        self._txtName = QtGui.QLabel(self)
        self._txtName.setGeometry(0, 0, 180, 20)
        self._txtName.setAlignment(QtCore.Qt.AlignCenter)

        self._img = QtGui.QLabel(self)
        self._img.setGeometry(0, 20, 200, 300)
        self.data = None

    def updateInfo(self, animal):
        self.data = animal
        #update ui
        self._txtName.setText(u'<font size="4">%s</font>' % self.data.get('name', ''))
        self._downloadImg()

    def _downloadImg(self):
        if 'image' not in self.data:
            return
        self.imgPath = self._downloadMgr.download(self.data['image'])
        if self.imgPath:
            self._onImgLoaded(0, self.data['image'], self.imgPath)

    def _onImgLoaded(self, code, url, path):
        if code != 0:
            if 'image' in self.data and url == self.data['image']:
                print (u'图片下载出错')
            return
        if 'image' in self.data and url == self.data['image']:
            self.imgPath = path
            pixmap = QtGui.QPixmap(path)
            newpixmap = pixmap.scaledToHeight(self._img.height(), QtCore.Qt.SmoothTransformation)
            self._img.setPixmap(newpixmap)

    def setDownloadMgr(self, dm):
        self._downloadMgr = dm
        self._downloadMgr.downloadFinished.connect(self._onImgLoaded)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    wnd = SampleWgt()
    # wnd.loadFromUrl("http://p0.qhimg.com/t0185a14f94ff6aea0a.jpg")
    # wnd.setText('BUTTON')
    wnd.show()
    sys.exit(app.exec_())