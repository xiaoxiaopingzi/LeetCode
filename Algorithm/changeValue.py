# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: changeValue.py 
@time: 2018-04-24 15:11

交换A，B两个变量的值(在不引入其他变量的情况下)
"""


def swap1(A, B):
    print('A =', A, ',B =', B)
    A = A + B
    B = A - B
    A = A - B
    print('A和B的值交换后：')
    print('A =', A, ',B =', B)


def swap2(A, B):
    print('A =', A, ',B =', B)
    A = A * B
    B = A / B
    A = A / B
    print('A和B的值交换后：')
    print('A =', A, ',B =', B)


def swap3(A, B):
    print('A =', A, ',B =', B)
    A = A ^ B  # 异或
    B = A ^ B
    A = A ^ B
    print('A和B的值交换后：')
    print('A =', A, ',B =', B)


print('方法1：')
swap1(10, 38)
print('-------------------------------------')
print('方法2：')
swap2(10, 38)
print('-------------------------------------')
print('方法1：')
swap3(10, 38)
