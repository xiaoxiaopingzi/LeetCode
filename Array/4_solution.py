# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 4_solution.py 
@time: 2018-03-23 16:09

存在重复
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 使用set集合去重
        return len(set(nums)) != len(nums)


    # 方法2，先对数组进行排序，然后再判断是否有重复
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


solu = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 7]
print(solu.containsDuplicate(nums))
