# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main2.py 
@time: 2018-09-25 18:35  
"""

s1 = input()


def getLongestSubseq(s):
    if s == s[::-1]:
        return len(s)
    dp = [[1 for i in range(len(s))] for k in range(len(s))]
    for j in (range(len(s))):
        for i in range(j - 1, -1, -1):
            if s[i] == s[j]:
                if i + 1 <= j - 1:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][len(s) - 1]


print(getLongestSubseq(s1))
