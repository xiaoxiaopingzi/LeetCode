# -*- coding: UTF-8 -*-
# from collections import Counter
#
# k = int(input())
# str1 = input()
# str2 = input()
#
# resCount = 0
#
#
# def cut(s):
#     yiYouList = []
#     for i in range(len(s) - k + 1):
#         tempStr = s[i:i + k]
#         if tempStr not in yiYouList:
#             yiYouList.append(tempStr)
#     return yiYouList
#
#
# def cut2(s):
#     yiYouList2 = []
#     for i in range(len(s) - k + 1):
#         tempStr = s[i:i + k]
#         yiYouList2.append(tempStr)
#     return yiYouList2
#
#
# list_1 = cut(str1)
# print(list_1)
#
# list_2 = cut2(str2)
# map_2 = {}
# print(list_2)
# for i in list_2:
#     if i in map_2:
#         map_2[i] += 1
#     else:
#         map_2[i] = 1
#
# print(map_2)
#
# rescount = 0
# for i in list_1:
#     if i in map_2:
#         resCount += map_2[i]
# print(resCount)
from collections import Counter

n = int(input())
A = input()
B = input()


def cut(s):
    results = []
    for i in range(len(s) - n + 1):
        results.append(s[i:i + n])
    return results


list_A = Counter(cut(A))
list_B = Counter(cut(B))

set_A = set(list_A)
set_B = set(list_B)

inter = set_A.intersection(set_B)
count = 0

for elem in inter:
    count += list_B[elem]

print(count)
