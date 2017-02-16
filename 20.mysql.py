# coding=utf-8
__author__ = 'g7842'

'''
MySQL是Web世界中使用最广泛的数据库服务器。
SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
'''

import mysql.connector

#如果文件不存在，会自动在当前目录创建:
conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
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



'''使用SQLAlchemy—ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上'''
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()