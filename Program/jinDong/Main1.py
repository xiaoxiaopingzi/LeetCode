# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen
@file: Main.py
@time: 2018-09-05 15:51

"""

str1 = input()
str2 = input()

count = 0


def isXiangsi(str1, str2):
    myDict = {}
    for index, char in enumerate(str1):
        temp = str2[index]
        if char in myDict.keys():
            if myDict[char] is not temp:
                return False
        else:
            if temp in myDict.values():
                return False
            myDict[char] = temp
    return True


for i in range(len(str1) - len(str2) - 1):
    if isXiangsi(str1[i: i + len(str2)], str2):
        count += 1

print(count)
# print(isXiangsi('aba', 'xyx'))
