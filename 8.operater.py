# coding=utf-8
__author__ = 'g7842'


def str_2_int(string):
    if not str.isalnum(string):
        return 0
    else:
        length = len(string)
        num = 0
        for i in range(length):
            power = 10 ** (length - i - 1)
            num += int(string[i]) * power
        return num


def msz_str_2_time(msz):
    arr1 = str.split(msz, '.')
    time = int(arr1[1])
    ms = arr1[0]
    arr2 = str.split(ms, ':')
    time += int(arr2[0]) * 60 * 1000 + int(arr2[1]) * 1000
    return time

print(10**3)
print(10**(3-1))
print(str_2_int('100'))
print(int('100'))
print(float('100.22'))

print(msz_str_2_time('01:57.70'))

string = '[01:57.70]'
print(msz_str_2_time(string[1:len(string) - 1]))


import re
print(re.findall('\\[\\d{2}:\\d{2}\\.\\d{2}\\]', '[03:27.82][02:26.11][01:23.65]要是能重来 我要选李白'))

for a in range(10):
    print(a)
