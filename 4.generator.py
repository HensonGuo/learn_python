#-*- encoding:utf8 -*-

"""生成器"""

"""
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
"""

l = [a*a for a in range(10)]
print (l)

g = (a*a for a in range(10))
print(g.next())
print(g.next())

for n in g:
    print(n)

"""
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
"""

#定义一个generator，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print (o.next())
print (o.next())