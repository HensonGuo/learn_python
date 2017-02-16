# coding=utf-8

__author__ = 'g7842'

#字母和数字的转换
print(chr(65))
print(ord(u'A'))

#字符编码
print(u'中文'.encode('utf-8'))
print('\u8981\u5a36\u4f60\uff0c\u4e0d\u662f\u8bf4\u8bf4\u800c\u5df2')
print(u'\u8981\u5a36\u4f60\uff0c\u4e0d\u662f\u8bf4\u8bf4\u800c\u5df2')

# 字符串的格式化
# %d digit
s1 = '%d5'%2
print(s1)
s2 = '%d5-%d3'%(1,3)
print(s2)

# %f 浮点数float
s3 = '价格%f元'%1.56
print(s3)
s4 = '价格区间%f-%f'%(1.464, 2.557)
print(s4)

# %s string
s5 = '%s,world'%'hello'
print(s5)
s6 = '%s,world,%s'%('hello', 'michila')
print(s6)

# %x hexadecimal
s7 = '%x'%11110000
print(s7)

#混合适配
s8 = '%s的年龄是%d'%('Tom',18)
print(s8)

#strip,删除字符
hername = 'abc'
char = hername.strip('ab')
print(char)
print(hername)


#center 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
test_str = 'rabcda'
print(test_str.center(8))
#capitalize 把字符串的第一个字符大写
print(test_str.capitalize())
test_str1 = u'你好'
print(test_str1.encode('utf-8'))

#count
print(test_str.count('a'))

#endswith
print('fsdf]'.endswith(']'))
#find
print('hellow index:%d' % 'abchellownihao'.find('hellow'))
#index
print('abcd'.index('c'))
#isalnum
print('fs32'.isalnum())
#isalpha
print(''.isalpha())
print('ba3'.isalpha())
print('fsd'.isalpha())
#isdigit
print('1345d'.isdigit())
print('34345'.isdigit())
#islower
print('ERfd'.islower())
print('dfg'.islower())
#isupper
print('FSDF'.isupper())
#isspace
print('3423 12'.isspace())
print(' '.isspace())



#join/upper/lower
print('ab'.join('cd'))
print('ab'.upper())
print('AB'.lower())
#partition
print('ab|cd'.partition('|'))
#split
print('a,b,c,d'.split(','))

#字符串切片
str1 = 'fsdfsdf'
print(str1[1:2])

print('1.2'.isalnum())
print('1.2'.isdigit())