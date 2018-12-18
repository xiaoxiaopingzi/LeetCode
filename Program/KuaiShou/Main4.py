# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main4.py 
@time: 2018-09-26 15:35  
"""
n = int(input())

dianQuan = list(map(int, input().split()))

dp = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    temp = 0
    for j in range(i + 1, n):
        if dianQuan[i] != dianQuan[j]:
            temp += 1
    dp[i][0] = temp
    dp[i][1] = temp

for i in range(n):
    for j in range(2, n):
        if dianQuan[i] == dianQuan[j]:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = dp[i][j - 1] - 1

resList = []

for i in range(n - 1):
    count = 0
    for j in range(i + 1):
        count += dp[i][j + 1]
    resList.append(str(count))

# for i in range(1, n):
#     count = 0
#     for j in range(1, i + 1):
#         for k in range(i + 1, n + 1):
#             if dianQuan[j - 1] != dianQuan[k - 1]:
#                 count += 1
#     resList.append(str(count))

print(' '.join(resList))
