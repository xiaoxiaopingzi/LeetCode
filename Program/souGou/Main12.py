# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main12.py 
@time: 2018-09-15 11:46  
"""


def bubble_sort(s, f):
    for i in range(len(f)):
        for j in range(0, len(f) - i - 1):
            if f[j] > f[j + 1]:
                f[j], f[j + 1] = f[j + 1], f[j]
                s[j], s[j + 1] = s[j + 1], s[j]
    return s, f


def greedy(s, f, n):
    a = [True for x in range(n)]
    j = 0
    for i in range(1, n):
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a


n = int(input())
s = []
f = []
for i in range(int(n / 2)):
    start = float(input())
    end = float(input())
    s.append(start)
    f.append(end)

s, f = bubble_sort(s, f)
A = greedy(s, f, int(n / 2))

res = []
for k in range(len(A)):
    if A[k]:
        res.append('({},{})'.format(s[k], f[k]))
print(int(n / 2) - len(res))
