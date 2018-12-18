# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-10-21 10:29  
"""

m = int(input())

for i in range(m):
    s = input()
    indexOfHW = []
    for j in range(1, len(s)):
        if s[j].isupper():
            if len(indexOfHW) == 0 or (j < len(s) - 1 and s[j + 1].islower()):
                indexOfHW.append(j)
    # print(indexOfHW)
    if len(indexOfHW) == 0:
        print(s.lower())
    else:
        returnS = ''
        for index in range(len(indexOfHW) + 1):
            if index == 0:
                returnS += s[:indexOfHW[index]].lower() + '_'
            elif index == len(indexOfHW):
                returnS += s[indexOfHW[index - 1]:].lower()
            else:
                returnS += s[indexOfHW[index - 1]:indexOfHW[index]].lower() + '_'
        print(returnS)
