# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 4.2-QuickSort.py 
@time: 2018-11-13 9:55  
"""

arrs = [3, 67, 32, 543, 324, 354, 5, 652, 45]


def quickSort(arrs):
    if len(arrs) < 2:
        return arrs
    else:
        target = arrs[0]
        left = [i for i in arrs[1:] if i < target]
        right = [i for i in arrs[1:] if i >= target]
        return quickSort(left) + [target] + quickSort(right)


print(quickSort(arrs))
print(sorted(arrs))
