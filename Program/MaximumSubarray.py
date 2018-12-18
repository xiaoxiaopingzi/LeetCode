# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: MaximumSubarray.py 
@time: 2018-09-08 9:11  
"""
import sys


class Solution:
    def maxSubArray(self, nums):
        maxVlaue = -sys.maxsize
        subSum = 0
        for i in nums:
            if subSum < 0:
                subSum = i
            else:
                subSum += i
            if subSum > maxVlaue:
                maxVlaue = subSum
        return maxVlaue
