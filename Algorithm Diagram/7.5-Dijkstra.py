# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 7.5-Dijkstra.py
@time: 2018-11-13 10:21

狄克斯特拉算法 —— 求带权图的最短路径算法(图中不能有负权边)
"""
# 定义图
graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['finish'] = 1

graph['b'] = {}
graph['b']['finish'] = 5
graph['b']['a'] = 3

graph['finish'] = {}  # 终点没有任何邻居

# 定义开销
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity

#  定义存储父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = None


# 找到开销最小的节点
def find_lowest_cost_node(costs, processed):
    minValue = infinity
    node = None
    for key in costs.keys():
        if costs[key] < minValue and key not in processed:
            minValue = costs[key]
            node = key
    return node


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighs = graph[node]
        for n in neighs.keys():
            if cost + neighs[n] < costs[n]:
                costs[n] = cost + neighs[n]
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


dijkstra(graph, costs, parents)
print(costs)
print(parents)
