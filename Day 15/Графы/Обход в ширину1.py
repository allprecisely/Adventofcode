# Я это сделал это сам!!!! Просто зная идею!!!!
# Начало положено, тут рабочий обход в ширину со стенками

from collections import deque

start = (4,4)
deq = deque()
vertexes = {}
visited = []
S = {start: 0}
deq.append(start)
walls = [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(6,4), (6,5), (6,6), (2,4), (2,5), (1,5), (0,5)]

for i in range(8):
    for j in range(8):
        vertexes[i,j] = set()

for i in range(0, 8):
    for j in range(0, 8):
        if i - 1 >= 0 and (i-1,j) not in walls:
            vertexes[i, j].add((i-1,j))
        if i + 1 < 8 and (i+1,j) not in walls:
            vertexes[i, j].add((i+1,j))
        if j - 1 >= 0 and (i,j-1) not in walls:
            vertexes[i, j].add((i,j-1))
        if j + 1 < 8 and (i,j+1) not in walls:
            vertexes[i, j].add((i,j+1))

while len(deq) > 0:
    tmp = deq.popleft()
    visited.append(tmp)
    for i in vertexes[tmp]:
        if i not in visited:
            S[i] = S[tmp] + 1 if S.get(i, float('inf')) > S[tmp] + 1 else S[i]
            deq.append(i)

for i in range(0, 8):
    print()
    for j in range(0, 8):
        print(S.get((i,j), '#'), end = ' ')
