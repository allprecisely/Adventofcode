def puzzle(inp):
    s2 = 0
    s3 = 0
    with open(inp) as f:
        for i in f.readlines():
            dct = dict()
            for l in i:
                dct[l] = dct.get(l, 0) + 1
            if 2 in dct.values():
                s2 += 1
            if 3 in dct.values():
                s3 += 1
    return s2*s3


print(puzzle('input.txt'))