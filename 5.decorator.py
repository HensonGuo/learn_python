#-*- encoding:utf8 -*-

"""装饰器"""

"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。函数对象有一个__name__属性，可以拿到函数的名字：
"""

def now():
    print '2013'

f = now
f()
print f.__name__


"""
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
"""

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

"""
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
"""
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()


"""类装饰器"""

def singleton(cls):
    def getinstance():
        if cls not in singleton.instances:
            singleton.instances[cls] = cls()
        return singleton.instances[cls]
    return getinstance


singleton.instances = {}


@singleton
class Handler(object):

    def trace(self):
        print('abc')


Handler().trace()
Handler().trace()

SALEID_2_WIDGET_CLASS = {}

#传递参数的，参考函数装饰器
def registerTip(saleid=0):
    def decorate(tipClass):
        SALEID_2_WIDGET_CLASS.update({saleid: tipClass})
        return tipClass
    return decorate

