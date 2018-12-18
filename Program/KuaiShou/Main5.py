# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main5.py 
@time: 2018-09-26 15:48  
"""


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getCircle(p1, p2, p3):
    x21 = p2.x - p1.x
    y21 = p2.y - p1.y
    x32 = p3.x - p2.x
    y32 = p3.y - p2.y
    # three colinear
    if x21 * y32 - x32 * y21 == 0:
        return None
    xy21 = p2.x * p2.x - p1.x * p1.x + p2.y * p2.y - p1.y * p1.y
    xy32 = p3.x * p3.x - p2.x * p2.x + p3.y * p3.y - p2.y * p2.y

    y0 = (x32 * xy21 - x21 * xy32) / 2 * (y21 * x32 - y32 * x21)
    x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
    R = ((p1.x - x0) ** 2 + (p1.y - y0) ** 2) ** 0.5

    return x0, y0, R


# p1, p2, p3 = Point(0, 0), Point(4, 0), Point(2, 2)
# print(getCircle(p1, p2, p3))

n, m = map(int, input().split())

arrs = []

for i in range(n):
    temp = list(map(int, input().split()))
    arrs.append(temp)

poits = []
for i in range(n):
    temp = arrs[i][:]
    count = 0
    index = 0
    for j in temp:
        if j == 1:
            count += 1
            index = j
    if count == 1:
        poits.append(Point(i, index))

for i in range(n):
    temp = arrs[:][i]
    count = 0
    index = 0
    for j in temp:
        if j == 1:
            count += 1
            index = j
    if count == 1:
        poits.append(Point(i, index))

x0, y0, r = getCircle(poits[0], poits[1], poits[2])
print(x0, y0)
