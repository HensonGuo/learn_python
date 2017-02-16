__author__ = 'g7842'

from math import cos, sin, pi


for i in range(0, 6):
    arc = (30 + 60 * i) * pi / 180
    aa = cos(arc)
    # print(aa)
    print(round(aa, 2))


for i in range(0, 6):
    arc = (30 + 60 * i) * pi / 180
    aa = sin(arc)
    # print(aa)
    print(round(aa, 2))

print(sin(45 * pi / 180) * 34)
