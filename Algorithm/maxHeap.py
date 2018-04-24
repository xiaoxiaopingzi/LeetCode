# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: maxHeap.py 
@time: 2018-04-23 22:15

最大堆：
    1、每个子节点都不大于其父节点
        如果子节点为 k,则父节点为 k//2，如果父节点为k,则左子节点为 2*k, 右子节点为 2*k+1,
    3、二叉堆是完全二叉树
        完全二叉树表示每层的非叶子节点数都为2的倍数，最后一层的叶子节点全部位于树的左侧
"""
import random


class MaxHeap(object):
    def __init__(self):
        self.data = [0]
        self.count = 0

    def count(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    def shiftUp(self, k):
        while k > 1 and self.data[k] > self.data[k // 2]:
            self.swap(k, k // 2)
            k = k // 2

    def insert(self, num):
        self.count += 1
        self.data.append(num)
        self.shiftUp(self.count)


maxheap = MaxHeap()
for i in range(15):
    maxheap.insert(random.randint(0, 100))
print(maxheap.data)
