# coding=utf-8
__author__ = 'g7842'

#提供了常见的摘要算法，如MD5，SHA1
#摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难


#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
import hashlib
md = hashlib.md5()
md.update('how to use md5 in python hashlib?')
print md.hexdigest()

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md.update('how to use md5 in ')
md.update('python hashlib?')
print(md.hexdigest())



#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长
sha1 = hashlib.sha1()
sha1.update('how to use md5 in ')
sha1.update('python hashlib?')
print(sha1.hexdigest())


#摘要算法应用
#网站都会存储用户登录的用户名和口令
#如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里
#正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5