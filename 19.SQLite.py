# coding=utf-8
__author__ = 'g7842'

"""
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用
"""

import sqlite3

#如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')

#执行查询语句:
cursor.execute('select * from user where id=?', ('1', ))
res = cursor.fetchall()
if res:
    print(res)
else:
    # 若果不存在该记录插入一条记录:
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()
