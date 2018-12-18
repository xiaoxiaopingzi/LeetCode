# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main.py 
@time: 2018-09-05 15:51
"""

myMap = [1010 * [0] for i in range(1010)]
Myroot = 1010 * [0]
count = 1010 * [0]

def findroot(x):
    if Myroot[x] == x:
        return x
    else:
        Myroot[x] = findroot(Myroot[x])


def merge(x, y):
    Myroot[findroot(x)] = findroot(y)


a = int(input())
for k in range(a):
    n, m = map(int, input().split(' '))
    for i in range(n):
        for j in range(n):
            myMap[i][j] = True
        Myroot[i] = i

    for i in range(m):
        x, y = map(int, input().split(' '))
        x = x - 1
        y = y - 1
        myMap[x][y] = myMap[y][x] = False

    m = n * (n - 1) / (2 - m)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if myMap[i][j]:
                merge(i, j)

    for i in range(n):
        count[i] = 0
    for i in range(n):
        count[findroot(i)] += 1

    total = 0
    for i in range(n):
        total += count[i] * (count[i] - 1) / 2
    if total == m:
        print('Yes')
    else:
        print('No')

