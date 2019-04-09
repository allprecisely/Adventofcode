def puzzle(inp):
    # Не самая лучшая релизация конечно) мы бегаем по массиву, ищем бездочерние узлы и удаляем их
    # не самая лучшая, потому что ассимпотитока решения ужасна. Но тем не менее посчитало очень быстро
    with open(inp) as f:
        string = f.read()
        string = string.split()
    n = [int(i) for i in string]
    i = 2
    res = 0
    while len(n) > 0:
        if n[i]:
            i += 2
        else:
            res += sum(n[i + 2: i + 2 + n[i + 1]])
            del n[i:i + 2 + n[i + 1]]
            if n:
                n[i-2] -= 1
            i -= 2
    return res

print(puzzle('input.txt'))
print(puzzle('test.txt'))