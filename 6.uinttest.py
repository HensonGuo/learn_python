# coding=utf-8
__author__ = 'g7842'

import unittest

#setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。


class MyTest(unittest.TestCase):

    def setUp(self):
        print('setUp..')

    def tearDown(self):
        print('tear down..')

    def test_main(self):
        print('main')

    def test_a(self):
        print('excute a')

    def test_b(self):
        print('excute b')

    def cannotbe_test(self):
        print('要以test_为前缀，没被执行啊，你妹的')

if __name__ == '__main__':
    unittest.main()
