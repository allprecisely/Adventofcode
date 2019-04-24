# Существа оживают и идут друг к другу

from collections import deque
conter = {'G': 'E', 'E': 'G'}
flag = True

with open('test.txt') as f:
    strings = f.readlines()
arr1 = [list(i.replace('\n', '')) for i in strings]

def find_everybody(arr):
    creatures = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in 'EG':
                creatures.append({'pos': (i, j), 'HP': 200, 'race': arr[i][j]})
    return creatures

def graph_creation(arr):
    graph = {}

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            graph[i, j] = set()

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            if arr[i - 1][j] in '.EG':
                graph[i, j].add((i - 1, j))
            if arr[i + 1][j] in '.EG':
                graph[i, j].add((i + 1, j))
            if arr[i][j - 1] in '.EG':
                graph[i, j].add((i, j - 1))
            if arr[i][j + 1] in '.EG':
                graph[i, j].add((i, j + 1))

    return graph

def find_way(graph, start, race):
    deq = deque()
    deq.append(start)
    W = {start: None}
    way = []

    while len(deq) > 0:
        tmp = deq.popleft()
        if arr1[tmp[0]][tmp[1]] == race:
            break
        for i in graph[tmp]:
            if i not in W:
                W[i] = tmp
                deq.append(i)

    while True:
        way += [tmp]
        tmp = W.get(tmp, None)
        if tmp == start:
            break

    return way

units = find_everybody(arr1)

while flag:
    units.sort(key=lambda unit: unit['pos'])
    for i in range(len(units)):
        graph = graph_creation(arr1)
        way = find_way(graph, units[i]['pos'], conter[units[i]['race']])
        if len(way) <= 1:
            flag = False
            break
        arr1[units[i]['pos'][0]][units[i]['pos'][1]] = '.'
        arr1[way[-1][0]][way[-1][1]] = units[i]['race']
        units[i]['pos'] = way.pop()


    for i in range(len(arr1)):
        print()
        for j in range(len(arr1[0])):
            print(arr1[i][j], end=' ')
    print()
