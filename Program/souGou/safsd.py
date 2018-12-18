# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: safsd.py 
@time: 2018-09-15 21:22  
"""


def getLcsOfLength(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    dp = [[0 for _ in range(len(strB) + 1)] for _ in range(len(strA) + 1)]
    for i in range(1, len(strA) + 1):
        for j in range(1, len(strB) + 1):
            if strA[i - 1] == strB[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max([dp[i - 1][j], dp[i][j - 1]])
    print(dp[len(strA)][len(strB)])
    # 输出最长公共子序列
    # i, j = len(strA), len(strB)
    # LCS = ""
    # while i > 0 and j > 0:
    #     # 这里一定要比较a[i-1]和b[j-1]是否相等
    #     if strA[i - 1] == strB[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
    #         LCS = strA[i - 1] + LCS
    #         i, j = i - 1, j - 1
    #         continue
    #     if dp[i][j] == dp[i - 1][j]:
    #         i, j = i - 1, j
    #         continue
    #     if dp[i][j] == dp[i][j - 1]:
    #         i, j = i, j - 1
    #         continue
    # print("LCS is :", LCS)


strA = input()
strB = input()
getLcsOfLength(strA, strB)
