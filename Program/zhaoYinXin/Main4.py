# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main3.py 
@time: 2018-09-16 18:43  
"""
import functools

N = int(input())
arrs = []

for i in range(N):
    tempList = list(map(int, input().split('.')))
    arrs.append(tempList)
# print(arrs)


def biJiao(list1, list2):
    length = min(len(list2), len(list1))
    for i in range(length):
        if list1[i] < list2[i]:
            return -1
        elif list1[i] > list2[i]:
            return 1
        else:
            continue
    if len(list1) > len(list2):
        return 1
    elif len(list1) < len(list2):
        return -1
    else:
        return 0


arrs = sorted(arrs, key=functools.cmp_to_key(biJiao))
# print(arrs)

for i in arrs:
    i = map(str, i)
    print('.'.join(i))