# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: EditDistance.py 
@time: 2018-09-08 9:20
编辑距离

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        # value = [[0] * 4] * 3
        # 这虽然能产生3行4列的二维数组，但在修改数组内容时发现：同一列的数据会同时改变
        # m + 1 行， n + 1 列
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, n + 1):
            dp[0][i] = i
        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                insertion = dp[i][j - 1] + 1
                delte = dp[i-1][j] + 1

                temp = 1
                if word1[i - 1] == word2[j - 1]:
                    temp = 0
                replace = dp[i-1][j-1] + temp

                dp[i][j] = min(insertion, delte, replace)

        return dp[m][n]


solu = Solution()
print(solu.minDistance("ro", "ros"))