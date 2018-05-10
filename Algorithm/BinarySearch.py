# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: BinarySearch.py 
@time: 2018-04-23 20:59

二分查找法——指适合有序的数组

时间复杂度为 O(logn)
"""


# 在有序的数组中查找target
def binarySearch(arr, target):
    L = 0
    r = len(arr) - 1
    # 注意当L和r都达到了整数的最大值，middle = (L + r) / 2会出现溢出的情况，所以不能使用这种方式
    # middle = (L + r) / 2
    middle = L + (r - L) / 2
    while L <= r:
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            L = middle + 1
        else:
            r = middle - 1
    return -1


# 二分查找法的递归版本
def binarySearch2(arr, L, r, target):
    middle = L + (r - L) / 2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binarySearch2(arr, middle + 1, r, target)
    else:
        return binarySearch2(arr, L, middle - 1, target)


# 二分查找法, 在有序数组arr中, 查找target
# 如果找到target, 返回第一个target相应的索引index
# 如果没有找到target, 返回比target小的最大值相应的索引, 如果这个最大值有多个, 返回最大索引
# 如果这个target比整个数组的最小元素值还要小, 则不存在这个target的floor值, 返回-1
# def floor(arr, target):
