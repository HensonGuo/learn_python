#-*- encoding:utf-8 -*-
__author__ = 'g7842'

import codecs
import time
import sys,os, csv, cStringIO

def mb_code(string, coding="utf-8"):
    if isinstance(string, unicode):
        return string.encode(coding)
    for c in ('utf-8', 'gb2312', 'gbk', 'gb18030', 'big5'):
        try:
            return string.decode(c).encode(coding)
        except:
            pass
    return string

#保存unicode格式
def saveUnicode(content, filePath):
    fh = codecs.open(filePath,"w","utf-16")
    fh.write(content.decode("utf-8"))
    fh.close()

#保存ANSI格式
def saveAnsi(content, filePath):
    fh = codecs.open(filePath,"w","GBK")
    fh.write(content.decode("utf-8"))
    fh.close()

#保存utf-8格式
def saveUtf8(content, filePath):
    fh = codecs.open(filePath,"w","UTF-8")
    fh.write(content.decode("utf-8"))
    fh.close()


def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()

def WriteFile(filePath,u,encoding="gbk"):
    with codecs.open(filePath,"wb") as f:
        f.write(u.encode(encoding,errors="ignore"))

def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gb18030")


if __name__ == '__main__':
        #todo 重新写个类 非二进制
        datalist = [[u'1', u'张三']]
        # UTF8_2_GBK('E:/test.csv', 'E:/test1.csv')
        # UTF8_2_GBK('E:/a.txt', 'E:/b.txt')
        # saveAnsi('你好', 'E:/ansi.txt')
