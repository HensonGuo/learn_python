# coding=utf-8
__author__ = 'g7842'

# *表示任意个字符（包括0个）
# +表示至少一个字符
# ?表示0个或1个字符
# {}个数范围，{n}表示n个字符，用{n,m}表示n-m个字符：
# []取值范围

# \d可以匹配一个数字，
# \w可以匹配一个字母或数字
# \s可以匹配一个空格

#'-'是特殊字符，在正则表达式中，要用'\'转义
#sample:
    # [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
    # [0-9a-zA-Z\_]+可以匹配至少由一个数字、
    # [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
    # [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

# A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束



#使用Python的r前缀，就不用考虑转义的问题了
s = r'abc\fsdf'
print(s)

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print 'ok'
else:
    print 'failed'

#split 切分字符串
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))

#分组 用()表示的就是要提取的分组（Group）。比如：^(\d{3})-(\d{3,8})$分别定义了两个组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(0,1))

#贪婪匹配 也就是匹配尽可能多的字符
m = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(m)

#编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()
re_telephone.match('010-8086').groups()

print u'\u5b98\u7f51\u6d3b\u52a8\u8bf4\u660e'