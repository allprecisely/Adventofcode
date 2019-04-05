import re

def puzzle(inp):
    with open(inp) as f:
        arr = f.readlines()
    pat = re.compile(r'\[(\d+-\d+-\d+) (\d+):(\d+)\] (\w+) #?(\d+)?.*?')
    arr.sort()
    d = dict()
    for i in arr:
        data = pat.search(i)
        if data.group(4) == 'Guard':
            guard = data.group(5)
            if guard not in d:
                d[guard] = {i: 0 for i in range(60)}
        elif data.group(4) == 'falls':
            start = int(data.group(3))
        else:
            for j in range(start, int(data.group(3))):
                d[guard][j] += 1
    counter = 0
    for key, value in d.items():
        tmp = max(value.values())
        if tmp > counter:
            counter = tmp
            guard = key
    counter = 0
    for i in range(60):
        if d[guard][i] > counter:
            counter = d[guard][i]
            day = i
    return int(guard) * day



print(puzzle('input.txt'))