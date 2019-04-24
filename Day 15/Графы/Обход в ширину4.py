# Я это сделал это сам!!!! Просто зная идею!!!!
# Тут планирую прочитать внешний файл, и уже пойти по реальной карте

from collections import deque

with open('test.txt') as f:
    strings = f.readlines()
arr = [list(i) for i in strings]
start = (2,4)
end = (5, 1)

while abs(start[1]-end[1])+abs(start[0]-end[0]) > 1:
    deq = deque()
    vertexes = {}
    visited = []
    S = {start: 0}
    W = {start: []}
    deq.append(start)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            vertexes[i, j] = set()
            W[i, j] = list()

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i - 1][j] == '.':
                vertexes[i, j].add((i - 1, j))
            if arr[i + 1][j] == '.':
                vertexes[i, j].add((i + 1, j))
            if arr[i][j - 1] == '.':
                vertexes[i, j].add((i, j - 1))
            if arr[i][j + 1] == '.':
                vertexes[i, j].add((i, j + 1))

    while len(deq) > 0:
        tmp = deq.popleft()
        if tmp == end:
            break
        visited.append(tmp)
        for i in vertexes[tmp]:
            if i not in visited:
                if S.get(i, float('inf')) > S[tmp] + 1:
                    S[i] = S[tmp] + 1
                    W[i] = W[tmp] + [tmp]
                deq.append(i)

    for i in W[end]:
        if S[i] == 1:
            arr[start[0]][start[1]] = '.'
            start = i
            arr[i[0]][i[1]] = 'E'
            break

    for i in range(len(arr)):
        print()
        for j in range(len(arr[0])):
            if (i,j) in W[end]:
                print('*', end = ' ')
            else:
                print(S.get((i,j), '#'), end = ' ')
    print()

# print()
# print(W)
