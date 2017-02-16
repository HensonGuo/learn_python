# coding=utf-8
__author__ = 'g7842'


class Student(object):
    #限制属性的添加；节省内存
    #__slots__ = ('__name', '__age', '__skill', 'nick', 'heigt', 'weight', 'score', '__count')

    #staticvar是类变量，可以由类名直接调用，也可以有对象来调用
    staticvar = 0

    def __init__(self, name, age, nick):
        self.__name = name
        self.__age = age
        self.__nick = nick
        self.__skill = '杨门'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return "名字：%s  年龄：%d"%(self.__name, self.__age)

    def __len__(self):
        return 172

    #作为属性访问
    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, skill):
        self.__skill = skill

    #自身迭代，设置__iter__和next方法
    def __iter__(self):
        return self

    def next(self):
        self.__age += 1
        if self.__age > 20:
            raise StopIteration()
        return self

    #全局变量测试
    #类成员方法测试
    def test_func(self):
        self.staticvar += 1
        print('实例成员变量1:%d' % self.staticvar)
        print('实例成员变量2:%s' % self.__name)

    def test_func_first(self):
        #变量不能在初始化函数__init__外定义
        #self.var1 = 'var1'
        #self.var2 = 'var2'
        pass

    #静态方法测试
    @staticmethod
    def static_test_func(cls):
        #无self
        #self.staticvar
        #类.变量只能拥有函数外部
        #Student.staticvar
        cls.staticvar += 10
        print(cls.staticvar)