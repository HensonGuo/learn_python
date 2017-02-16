# coding=utf-8
__author__ = 'g7842'


#读取
try:
    f = open('_files/sample.txt', 'r')
    print(f.read())
finally:
    if f:
        #关闭节省内存资源
        f.close()

#简写方式
with open('_files/sample.txt', 'r') as outputfile:
    print(outputfile.read())


#读取行 readlines是读取的一个列表
with open('_files/sample.txt', 'r') as outputfile:
    for line in outputfile.readlines():
        print(line.strip())

#读取二进制文件
with open('_files/test.jpg', 'rb') as outputfile:
    print(outputfile.read())

#写入writelines
with open('_files/sample.txt', 'w') as outputfile:
    outputfile.writelines('fsdff\nfsdfsd')

#写入write
with open('_files/sample.txt', 'w') as outputfile:
    outputfile.write('fsdff\nfsdfsd')

import os

#系统
print(os.name)
print(os.environ)
print(os.environ.get('path'))

# 目录
abs_path = os.path.abspath('.')
print(abs_path)
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join(abs_path, 'testdir')
# 然后创建一个目录:
abs_path = abs_path.replace('\\', '/')
print(abs_path)
dir_path = '%s/testdir' % abs_path
#os.mkdir(dir_path)
#删除目录
#os.rmdir(dir_path)
#改变当前的目录
#os.chdir("/home/newdir")

#文件
#os.rename('_files/sample.txt', 'sample.txt')
#os.remove('sample.txt')

#拷贝粘贴
import shutil
shutil.copyfile('_files/sample.txt', 'sample.txt')

#分解文件路径
print(os.path.split(dir_path))
#分解文件扩展ming
print(os.path.splitext('_files/sample.txt'))


#过滤目录’.‘
print([x for x in os.listdir('.')])

#过滤文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

#显示当前的工作目录
print(os.getcwd())

f = file('_files/sample.txt','r')
#f.