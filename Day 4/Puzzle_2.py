def puzzle(inp):
    k = 0
    with open(inp) as f:
        arr = f.readlines()
    while True:
        mn = set()
        for i in arr:
            st = i[:k]+i[k+1:]
            if st in mn:
                return st
            mn.add(i[:k]+i[k+1:])
        k += 1


print(puzzle('input.txt'))