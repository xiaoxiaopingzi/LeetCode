# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: getKminNum.py 
@time: 2018-04-23 14:35

获取一个数组中第k小的数(k从1开始，到len(arr)结束)
获取一个数组中第k大的数(k从1开始，到len(arr)结束)
获取一个数组中前k小的数(k从1开始，到len(arr)结束)
"""


# 返回一个数组中最小的数，其最优的算法的复杂度是O(n)，需要进行n-1次比较
def getMinNum(arr):
    min = arr[0]
    for i in arr[1:]:
        if i < min:
            min = i
    return min


def swap(arr, L, j):
    temp = arr[L]
    arr[L] = arr[j]
    arr[j] = temp


# arr[L+1,...,j] < v， arr[j+1,...,i] > v
def paitition(arr, L, r):
    v = arr[L]  # 选择数组的第一个元素作为标定点
    j = L  # arr[L+1,...,j]表示小于v的元素
    for i in range(L + 1, r + 1):
        if arr[i] < v:
            swap(arr, j + 1, i)
            j += 1
    swap(arr, L, j)
    return j  # 索引j就表示v在排序好的数组中的位置


# 获取数组中第i小的数，i从1开始
def getKminNum(arr, L, r, i):
    if L == r:
        return arr[L]
    q = paitition(arr, L, r)
    k = q - L + 1  # q位置的元素表示数组中第k小的数
    if k == i:  # 如果k==i，就表示q所在位置的元素就是数组中第i小的数
        return arr[q]
    elif k < i:  # 如果k<i，就表示数组中第i小的数一定位于arr[q+1,...r]中
        return getKminNum(arr, q + 1, r, i - k)
    else:  # 如果k>i，就表示数组中第i小的数一定位于arr[L,...q-1]中
        return getKminNum(arr, L, q - 1, i)


# 获取数组中第i大的数，i从1开始
def getKmaxNum(arr, L, r, i):
    if L == r:
        return arr[L]
    q = paitition(arr, L, r)
    k = r - q + 1  # q位置的元素表示数组中第k大的数
    if k == i:
        return arr[q]
    elif k > i:  # 如果k>i，就表示数组中第i大的数一定位于arr[q+1,...r]中
        return getKmaxNum(arr, q + 1, r, i)
    else:  # 如果k<i，就表示数组中第i大的数一定位于arr[L,...q-1]中
        return getKmaxNum(arr, L, q - 1, i - k)


# 获取数组中第i小的数的索引
def getKminIndexNum(arr, L, r, i):
    if L == r:
        return L
    q = paitition(arr, L, r)
    k = q - L + 1  # q位置的元素表示数组中第k小的数
    if k == i:  # 如果k==i，就表示q所在位置的元素就是数组中第i小的数
        return q
    elif k < i:  # 如果k<i，就表示数组中第i小的数一定位于arr[q+1,...r]中
        return getKminIndexNum(arr, q + 1, r, i - k)
    else:  # 如果k>i，就表示数组中第i小的数一定位于arr[L,...q-1]中
        return getKminIndexNum(arr, L, q - 1, i)


# 获取数组中前k小的数
def getBeforeKMinNum(arr, i):
    temp = getKminIndexNum(arr, 0, len(arr) - 1, i)
    return sorted(arr[0: temp+1])


# 获取数组中第i大的数的索引
def getKmaxIndexNum(arr, L, r, i):
    if L == r:
        return L
    q = paitition(arr, L, r)
    k = r - q + 1  # q位置的元素表示数组中第k大的数
    if k == i:
        return q
    elif k > i:  # 如果k>i，就表示数组中第i大的数一定位于arr[q+1,...r]中
        return getKmaxIndexNum(arr, q + 1, r, i)
    else:  # 如果k<i，就表示数组中第i大的数一定位于arr[L,...q-1]中
        return getKmaxIndexNum(arr, L, q - 1, i - k)


# 获取数组中前k大的数
def getBeforeKMaxNum(arr, i):
    temp = getKmaxIndexNum(arr, 0, len(arr) - 1, i)
    return sorted(arr[temp:])


if __name__ == "__main__":
    arr = [1, 4, 7, 84, 3, 2, 45, 46, 22, 28, 27, 4, 20, 423, 40, 34, 234, 51, 46, 57, 6, 34, 54, 23, 42, 3432]
    print(sorted(arr))
    k = 7
    print('第{}小的数为：'.format(k), getKminNum(arr, 0, len(arr) - 1, k))
    print('第{}大的数为：'.format(k), getKmaxNum(arr, 0, len(arr) - 1, k))
    print('前{}小的数为：'.format(k), getBeforeKMinNum(arr, k))
    print('前{}大的数为：'.format(k), getBeforeKMaxNum(arr, k))
