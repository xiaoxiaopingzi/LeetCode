# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 6.5-BFS.py 
@time: 2018-11-13 10:03

通过BFS来遍历图，以找到指定的对象
"""

# 通过字典建立图
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque


def is_seller(name):
    return name[-1] == 'm'


def BFS(name):
    queue = deque()
    queue.append(name)
    processed = []
    while len(queue) != 0:
        person = queue.pop()
        if person not in processed:
            if is_seller(person):
                print(person, 'is a mango seller!')
                return True
            else:
                queue.extend(graph[person])
                processed.append(person)
    return False


BFS('you')
