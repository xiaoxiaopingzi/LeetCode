# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 9_solution.py 
@time: 2018-04-03 21:30

两数之和

给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tempMap = {}
        for i, num in enumerate(nums):
            diffNumber = target - num
            # temp = tempMap.get(num)
            # if temp is not None:
            #     return temp, i
            # 如果num在tempMap中，表示num就是tempMap.get(num)索引所在的元素所缺少的那一部分
            if num in tempMap:
                return tempMap.get(num), i
            tempMap[diffNumber] = i




