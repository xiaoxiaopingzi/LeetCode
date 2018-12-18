# -*- coding: UTF-8 -*-
"""
@file: Main2.py
@time: 2018-09-18 19:25  
"""

n = int(input())


def count(n):
    if n < 1:
        return 0
    if n < 10:
        return 1
    count = 0
    mybase = 1
    round = n
    while round > 0:
        weight = round % 10
        round = round // 10
        count += round * mybase
        if weight == 1:
            count += (n % mybase) + 1
        elif weight > 1:
            count += mybase
        mybase *= 10

    return count


# number = ''.join(map(str, range(1, n + 1)))
# one_times = number.count('1')
print(count(n))
