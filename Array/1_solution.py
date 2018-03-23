# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 1_solution.py 
@time: 2018-03-23 9:27

从排序数组中删除重复项
给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。

不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

示例：

给定数组: nums = [1,1,2],

你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
不需要理会新的数组长度后面的元素
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        index = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i]
                index += 1
        nums[index] = nums[-1]  # 需要将nums数组的最后一个元素加上
        return index + 1

    # 直接使用Set集合进行去重
    def removeDuplicates2(self, nums):
        nums[:] = sorted(list(set(nums)))
        return len(nums)

    # 和我的想法类似，但是这个是将nums[k]直接看成另一个数组
    def removeDuplicates3(self, nums):
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return len(nums)


temp = Solution()
nums = [1, 1, 2, 3, 4, 4, 6]
print(temp.removeDuplicates(nums))
print(nums)
