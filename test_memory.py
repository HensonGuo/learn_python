# coding=utf-8
__author__ = 'g7842'

import gc
import memory_profiler
from memory_profiler import profile

@profile
def test():
    for i in range(999999,0,-1):
      s =  str(i) * i
      s = None
      gc.collect()

if __name__ == "__main__":
    test()