# Улучшение алгоритма

from collections import deque

with open('test.txt') as f:
    strings = f.readlines()
arr1 = [list(i) for i in strings]

start = (2,4)
end = (5, 1)

def graph_creation(arr):
    graph = {}

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            graph[i, j] = set()

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i - 1][j] == '.':
                graph[i, j].add((i - 1, j))
            if arr[i + 1][j] == '.':
                graph[i, j].add((i + 1, j))
            if arr[i][j - 1] == '.':
                graph[i, j].add((i, j - 1))
            if arr[i][j + 1] == '.':
                graph[i, j].add((i, j + 1))

    return graph

def find_way(graph, start, end):
    deq = deque()
    deq.append(start)
    W = {start: None}
    way = []

    while len(deq) > 0:
        tmp = deq.popleft()
        if tmp == end:
            break
        for i in graph[tmp]:
            if i not in W:
                W[i] = tmp
                deq.append(i)

    tmp = end
    while True:
        way += [tmp]
        tmp = W[tmp]
        if tmp == start:
            break

    return way

graph = graph_creation(arr1)

# for i in range(1):
