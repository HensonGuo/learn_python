__author__ = 'g7842'

import re


def getMiddleStr(self, content,startStr,endStr):
    patternStr = r'%s(.+?)%s'%(startStr,endStr)
    p = re.compile(patternStr,re.IGNORECASE)
    m= re.findall(p,content)
    return m