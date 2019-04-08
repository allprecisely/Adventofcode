def puzzle(inp):
    # Тут все грустно, потому что пока не решил
    with open(inp) as f:
        arr = f.readlines()
    d_lets = dict()
    res = 0
    elf1 = elf2 = elf3 = elf4 = elf5 = 0
    let1 = let2 = let3 = let4 = let5 = ''

    for i in range(len(arr)):
        let = arr[i].split()
        if let[1] not in d_lets:
            d_lets[let[1]] = set(), {let[7]}
            if let[7] not in d_lets:
                d_lets[let[7]] = {let[1]}, set()
            else:
                d_lets[let[7]][0].add(let[1])
        else:
            d_lets[let[1]][1].add(let[7])
            if let[7] not in d_lets:
                d_lets[let[7]] = {let[1]}, set()
            else:
                d_lets[let[7]][0].add(let[1])

    # for i, j in d_lets.items():
    #     print(i, j)

    count = len(d_lets)
    tmp = set()
    while 0 < count:
        flag = True
        for key, value in d_lets.items():
            if not value[0] and key not in tmp:
                if elf1 == 0:
                    elf1 = ord(key) - 4
                    let1 = key
                    tmp.add(key)
                elif elf2 == 0:
                    elf2 = ord(key) - 4
                    let2 = key
                    tmp.add(key)
                elif elf3 == 0:
                    elf3 = ord(key) - 4
                    let3 = key
                    tmp.add(key)
                elif elf4 == 0:
                    elf4 = ord(key) - 4
                    let4 = key
                    tmp.add(key)
                elif elf5 == 0:
                    elf5 = ord(key) - 4
                    let5 = key
                    tmp.add(key)

        while flag:
            if elf1:
                elf1 = elf1 - 1
                if elf1 == 0:
                    vacl = let1
                    flag = False
            if elf2:
                elf2 = elf2 - 1
                if elf2 == 0:
                    vacl = let2
                    flag = False
            if elf3:
                elf3 = elf3 - 1
                if elf3 == 0:
                    vacl = let3
                    flag = False
            if elf4:
                elf4 = elf4 - 1
                if elf4 == 0:
                    vacl = let4
                    flag = False
            if elf5:
                elf5 = elf5 - 1
                if elf5 == 0:
                    vacl = let5
                    flag = False
            res += 1
        print(res)

        for j in d_lets[vacl][1]:
            d_lets[j][0].discard(vacl)
        del d_lets[vacl]
        count -= 1
    print(d_lets)
    return res


print(puzzle('test.txt'))
print(puzzle('input.txt'))