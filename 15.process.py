# coding=utf-8
__author__ = 'g7842'

import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool, Queue
import os, time, random, subprocess


"""
fork
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
而子进程只需要调用getppid()就可以拿到父进程的ID。
"""

#Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

# print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。


"""
multiprocessing
"""

# print(multiprocessing.cpu_count())

def run_proc(name):
    print('run child process %s(%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('process will start')
    p.start()
    p.join()
    print('process end.')
    print('')


"""
Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
"""
def long_time_task(name):
    print('run task %s(%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    p = Pool()
    for n in range(5):
        p.apply_async(long_time_task, args=(n,))
    print('Waiting for all subprocesses done...')
    p.close()   #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.join()
    print('all subprocesses done')
    print('')


"""
进程间通信
multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
"""


def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw进程结束后继续往下执行:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()