# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: msad.py 
@time: 2018-09-15 20:31  
"""


# 判断是否为素数，如果是则返回True，不是则返回False
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())
count = 0
# temp = []
end = n // 2 + 1
for i in range(1, end):
    if isPrime(i):
        if isPrime(n - i):
            count += 1
            # temp.append((i, n - i))

print(count)
# print(temp)
