# coding=utf-8
__author__ = 'g7842'

#itertools提供了非常有用的用于操作迭代对象的函数

#count()会创建一个无限的迭代器
import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

#cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('abc')
# for n in cs:
#     print(n)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('a', 10)
# for n in ns:
#     print(n)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in ns:
#     print n

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
# for c in itertools.chain('ABC', 'abc'):
#     print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

#imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准
for x in itertools.imap(lambda x,y: x * y, [10, 20, 30], itertools.count(1)):
    print(x)

#ifilter()就是filter()的惰性实现。
# print(itertools.ifilter(None,[4,2,1]))