def func(n):
    arr = [0]*n[0]
    res = 0
    if n[0] == 0:
        buf = sum(n[2:2+n[1]])
        return (buf, n[1] + 2)
    rem = 2
    for i in range(n[0]):
        tup = func(n[rem:])
        arr[i] = tup[0]
        rem += tup[1]
    for i in range(rem,rem+n[1]):
        if n[i] <= n[0]:
            res += arr[n[i]-1]
        rem += 1
    return res, rem


def puzzle(inp):
    # Это решение еще страшнее)) но я его сделаль)
    with open(inp) as f:
        string = f.read()
        string = string.split()
    n = [int(i) for i in string]
    return func(n)


print(puzzle('input.txt'))
print(puzzle('test.txt'))