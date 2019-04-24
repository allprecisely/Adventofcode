# Я это сделал это сам!!!! Просто зная идею!!!!
# Тут точка идет по своей траектории до цели

from collections import deque


start = (4,4)
end = (2, 1)
while start[1]-end[1]+start[0]-end[0] > 1:
    deq = deque()
    vertexes = {}
    visited = []
    S = {start: 0}
    W = {start: []}
    deq.append(start)
    walls = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (2, 4), (2, 5), (1, 5),
             (0, 5)]

    for i in range(8):
        for j in range(8):
            vertexes[i, j] = set()
            W[i, j] = list()

    for i in range(0, 8):
        for j in range(0, 8):
            if i - 1 >= 0 and (i - 1, j) not in walls:
                vertexes[i, j].add((i - 1, j))
            if i + 1 < 8 and (i + 1, j) not in walls:
                vertexes[i, j].add((i + 1, j))
            if j - 1 >= 0 and (i, j - 1) not in walls:
                vertexes[i, j].add((i, j - 1))
            if j + 1 < 8 and (i, j + 1) not in walls:
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
            start = i
            break

    for i in range(0, 8):
        print()
        for j in range(0, 8):
            if (i,j) in W[end]:
                print('*', end = ' ')
            else:
                print(S.get((i,j), '#'), end = ' ')

# print()
# print(W)
