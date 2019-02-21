# coding=utf-8

#整除
print(8//2.2)
print(100 >> 1)
print(100 << 1)
#取反
print(~100)
#异或
print(7 ^ 1)


#iteritems
my_map = {'a': 1, "b": 2, "c": 3, "d": 4}
for v, k in my_map.iteritems():
    print(v, k)


for x in xrange(1, 2):
    print('---%d' % x)