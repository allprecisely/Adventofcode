def puzzle(inp):
    # Идея в том, что в каждой координате хранится кортеж 2 значений, первое из которых
    # номер точки, второе - расстояние до нее.
    # Откидывание решений с бескорнечностью осуществляется удалением значений для крайних точек
    with open(inp) as f:
        arr = f.readlines()
    max_x = max_y = 0
    d = dict()

    for i in range(len(arr)):
        x, y = arr[i].split(', ')
        arr[i] = int(x), int(y)
        max_x = max_x if max_x > int(x) else int(x)
        max_y = max_y if max_y > int(y) else int(y)

    for i in range(1, max_y + 1):
        for j in range(1, max_x + 1):
            d[(i, j)] = [len(arr), max_x+max_y]

    d_dots = {i: 0 for i in range(len(arr)+1)}

    for i in range(len(arr)):
        x, y = arr[i]
        for j in range(1, max_y+1):
            for k in range(1, max_x+1):
                if abs(x - k) + abs(y - j) < d[(j, k)][1]:
                    d_dots[i] += 1
                    d_dots[d[(j, k)][0]] -= 1
                    d[(j, k)][0] = i
                    d[(j, k)][1] = abs(x - k) + abs(y - j)
                elif abs(x - k) + abs(y - j) == d[(j, k)][1]:
                    d_dots[d[(j, k)][0]] -= 1
                    d[(j, k)][0] = len(arr)
                    d[(j, k)][1] = abs(x - k) + abs(y - j)

    for i in range(1, max_y+1):
        d_dots[d[(i, 1)][0]] = 0
        d_dots[d[(i, max_x)][0]] = 0
    for i in range(1, max_x+1):
        d_dots[d[(1, i)][0]] = 0
        d_dots[d[(max_y, i)][0]] = 0

    # for i in range(1, max_y+1):
    #     print()
    #     for j in range(1, max_x+1):
    #         print(d[(i, j)], end = ' ')

    return max(d_dots.values())


print(puzzle('input.txt'))