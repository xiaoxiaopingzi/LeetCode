# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen
@file: QuickSort.py
@time: 2018-04-23 14:00

快速排序的Python实现

时间复杂度为 O(nlogn)
"""
import random


def swap(arr, L, j):
    temp = arr[L]
    arr[L] = arr[j]
    arr[j] = temp


# arr[L+1,...,j] < v， arr[j+1,...,i] > v
def paitition(arr, L, r):
    # random.randint(a, b)-Return random integer in range [a, b], including both end points.
    swap(arr, L, random.randint(L + 1, r))
    v = arr[L]  # 选择数组的第一个元素作为标定点
    j = L  # arr[L+1,...,j]表示小于v的元素
    for i in range(L + 1, r + 1):
        if arr[i] < v:
            swap(arr, j + 1, i)
            j += 1
    swap(arr, L, j)
    return j  # 索引j就表示v在排序好的数组中的位置


# 对数组arr进行快速排序
def quickSort(arr, L, r):
    if L >= r:
        return
    p = paitition(arr, L, r)
    quickSort(arr, L, p - 1)
    quickSort(arr, p + 1, r)
    return arr


if __name__ == "__main__":
    arr = [1, 5, 7, 84, 3, 5, 45, 46, 7, 8, 23, 27, 23, 4, 23, 423, 42, 34, 234, 5, 46, 57, 6, 34, 54, 23, 42, 3432]
    print(quickSort(arr, 0, len(arr) - 1))
    print(help(random.randint))
