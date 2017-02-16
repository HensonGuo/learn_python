# coding=utf-8
__author__ = 'g7842'

"""迭代器"""

class Fabs(object):
    def __init__(self,max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1  #特别指出：第0项是0，第1项是第一个1.整个数列从1开始
    def __iter__(self):
        return self
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration() #越界抛出StopIteration异常

print Fabs(5)
for key in Fabs(5):
    print key

student = {'name':u'小米', 'age':10}
for key in student.__iter__():
    print(key)