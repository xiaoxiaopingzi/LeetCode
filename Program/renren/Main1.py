# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen
@file: Main.py
@time: 2018-09-05 15:51

"""

n, k = map(int, input().split())
arrs = list(map(int, input().split()))

arrs = sorted(arrs, reverse=True)
print(arrs[k-1])

