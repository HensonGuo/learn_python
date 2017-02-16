# coding=utf-8
__author__ = 'g7842'

"""
thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
主线程结束后，会默认等待子线程结束后，主线程才退出
"""

import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.currentThread().name, n))
        time.sleep(1)   #表示线程起挂的时间
    print('thread %s is ended' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
#jion的作用，是等待t线程结束后继续往下执行
t.join()
print('thread %s is ended' % threading.current_thread().name)


"""
*Lock
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量
"""

balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


# def run_thread(n):
#     for i in range(1000):
#         change_it(n)

def run_thread(n, thread_name):
    for i in range(1000):
        #先要获取锁:当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
        lock.acquire()
        try:
            change_it(n)
            # print('%s excute %d' % (thread_name, i))
        finally:
            # 改完了一定要释放锁:
            lock.release()
            pass

t1 = threading.Thread(target=run_thread, name='t1', args=(5, 't1'))
t2 = threading.Thread(target=run_thread, name='t2', args=(8,'t2'))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

"""
*ThreadLocal
一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程
但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
"""

local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

#全局变量local_school就是一个ThreadLocal对象，
# 每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.
# student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。


"""
多核CPU
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多
线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
"""


""""多线程pycharm调试
调试窗口Debugger-frames-右键（Focus on Startup）
"""