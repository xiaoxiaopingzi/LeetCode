# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 5_solution.py 
@time: 2018-03-23 16:16

只出现一次的数字
给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。


备注：

你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0与任何数异或后的结果是保持原来的数不变
        temp = 0
        for num in nums:
            temp = temp ^ num
        return temp


solu = Solution()
nums = [1, 1, 3, 2, 2]
print(solu.singleNumber(nums))
