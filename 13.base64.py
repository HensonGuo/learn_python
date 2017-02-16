# coding=utf-8
__author__ = 'g7842'

#base64
# Base64是一种用64个字符来表示任意二进制数据的方法
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
# 因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，
# 就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

import base64

print(base64.b64encode('binary/x00string'))
print(base64.b64decode('YmluYXJ5L3gwMHN0cmluZw=='))

with open('_files/test.jpg', 'rb') as f:
    print(base64.b64encode(f.read()))


#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode('i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64decode('646'))
print(base64.urlsafe_b64decode('abcd--__'))


#struct
#struct的pack函数把任意数据类型变成字符串
import struct
print(struct.pack('>I', 10240099))#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数