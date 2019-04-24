# Тут они начнут сражаться

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
            for k in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if arr[k[0]][k[1]] in '.EG':
                    graph[i, j].add(k)

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

def find_enemy(unit, enemy):
    i, j = unit['pos'][0], unit['pos'][1]
    enemies = []
    for k in (i-1,j), (i, j-1), (i, j+1), (i+1,j):
        for u in range(len(units)):
            if units[u]['pos'] == k and units[u]['race'] == enemy:
                enemies.append((units[u]['HP'], u))
                break
    aim = min(enemies)[1]
    units[aim]['HP'] -= 3
    if units[aim]['HP'] < 0:
        arr1[units[aim]['pos'][0]][units[aim]['pos'][1]] = '.'
        del units[aim]
        return True
    return False

# def fight(unit1, unit2):

units = find_everybody(arr1)

while flag:
    units.sort(key=lambda unit: unit['pos'])
    for i in range(len(units)):
        graph = graph_creation(arr1)
        way = find_way(graph, units[i]['pos'], conter[units[i]['race']])
        if len(way) <= 1:
            ft = find_enemy(units[i], conter[units[i]['race']])
            if ft:
                flag = False
            break
        arr1[units[i]['pos'][0]][units[i]['pos'][1]] = '.'
        arr1[way[-1][0]][way[-1][1]] = units[i]['race']
        units[i]['pos'] = way.pop()
        i += 1

    for i in range(len(arr1)):
        print()
        for j in range(len(arr1[0])):
            print(arr1[i][j], end=' ')
    print()
