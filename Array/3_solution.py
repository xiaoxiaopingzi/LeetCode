# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 3_solution.py 
@time: 2018-03-23 12:35

旋转数组
将包含 n 个元素的数组向右旋转 k 步。

例如，如果n = 7, k = 3，给定数组[1,2,3,4,5,6,7]，向右旋转后的结果为[5,6,7,1,2,3,4]。

"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
            return
        # 可能出现k大于len(nums)的情况，所以需要先求k对len(nums)的余数
        temp1 = k % len(nums)
        # temp值就是前两次翻转的中心
        temp = len(nums) - temp1 - 1
        # 三次翻转
        self.turn(0, temp, nums)
        self.turn(temp + 1, len(nums) - 1, nums)
        self.turn(0, len(nums) - 1, nums)

    def turn(self, start, end, nums):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    # 直接使用列表的切片进行旋转
    def rotate2(self, nums, k):
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


solu = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(solu.rotate(nums, 3))
print(nums)
