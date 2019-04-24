from collections import deque

# ух.. задачу уже с ходу конечно не взять, как я привык...
# разобрать обход в ширину: 1) пустой квадрат 5х5; 2) с препядствиями; 3) с недостижимыми клетками
# два предстваителя движуться на встречу друг другу, с препядствиями
# больше, чем 2 представителя

def puzzle(inp):
    #

    with open(inp) as f:
        strings = f.readlines()
    arr = [list(i) for i in strings]

    elfs = []
    goblins = []
    creatures = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'E':
                creatures.append({'pos': [i, j], 'race': arr[i][j]})
                elfs.append({'pos': [i, j], 'HP': 200, 'targ': [0,0]})
            elif arr[i][j] == 'G':
                creatures.append({'pos': [i, j], 'race': arr[i][j]})
                goblins.append({'pos': [i, j], 'HP': 200, 'targ': [0,0]})

    distance = [None] * len(arr)*len(arr[0])

    graph = dict()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            graph[(i,j)] = set()

    def add_edge(v1, v2):
        graph[v1].add(v2)
        graph[v2].add(v1)

    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            for k in i+1,i-1:
                if k == '.':
                    add_edge((i,j),(k,j))
            for k in j + 1, j - 1:
                if k == '.':
                    add_edge((i,j),(i,k))


def calc_route(creatures):
    while True:
        creatures.sort(key=lambda unit: unit['pos'])
        for unit in creatures:
            if unit['race'] == 'E':
                pass

print(puzzle('test1.txt'))


# print(puzzle('input.txt'))
