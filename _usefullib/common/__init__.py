#-*- encoding:utf8 -*-
__author__ = 'g7842'

from PyQt4 import QtCore, QtGui

"""
1.处理异常字符
label = QtGui.QLabel()
label.setTextFormat(QtCore.Qt.PlainText)"""

"""
2.tips抢焦点设置
self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
self.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
"""

"""
4.文本行距设置
u'<p style="line-height:20px;font-size:12.5px;">'
"""

"""
5.TIPS
self._tip = QtGui.QLabel(self)
self._tip.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.ToolTip)
self._tip.setWordWrap(True)
self._tip.setObjectName('tip')
self._tip.setVisible(False)
self._tip.setStyleSheet("QWidget#tip{border:1px solid #84b8ec;background-color:#ffffff;padding:4,4,4,4;}")
"""

"""
6.超链接文本及Img标签
self._channel.setText(u'<img src="%s"/><font color="#ffffff" face="宋体"> %d频道正在抽金币，</font>
<a href=www.netease.com><font color="#fee014">我也要抽</font></a>' %
(RollingChannels.TrumpetIcon, room_id))
"""

"""
7.注册表使用
setting = QtCore.QSettings('CC', 'luckyGift')
notNotify = setting.value('versionUpdateNofify', QtCore.QVariant(0)).toInt()[0] == 1
setting.setValue('versionUpdateNofify', QtCore.QVariant(1))
if notNotify:
return
"""

"""
8.拖拽
def winEvent(self, MSG):
     if WM_NCHITTEST == MSG.message:
        pos = QtGui.QCursor.pos()
        pos = self.webView.mapFromGlobal(pos)
        if self.isWebCaption(pos.x(), pos.y()):
            return True, HTCAPTION
    return super(CommonWebWindow, self).winEvent(MSG)
"""