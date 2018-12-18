# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main.py 
@time: 2018-09-05 15:51
"""
A = input()
B = input()
Q = int(input())
dp = len(A) * [0]

for i in range(len(B) - 1, len(A)):
    if A[i - len(B) + 1:i + 1] == B:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

for i in range(Q):
    l, r = map(int, input().split(' '))
    print(dp[r - 1] - dp[l - 1])
