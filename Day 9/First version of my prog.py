def puzzle(inp):
    #
    with open(inp) as f:
        string = f.read()
        string = string.split()
    p, m = int(string[0]), int(string[6]) - 1
    arr = [0, 1]
    i = 2
    k = 0
    d = {x: 0 for x in range(p)}
    tmp = 1
    while m != 0:
        for j in range(k, len(arr)-k):
            if i%23 == 0:
                print(i, (i - 2) % p + 1, arr, max(d.values()))
                tmp = 0 if tmp == 1 else 1
                d[i % p] += arr.pop(2*(j-1) - 6 - tmp) + i
                print(i, i % p, arr, max(d.values()))
                print()
                k = (2*(j-1) - 4 - tmp)//2 if 2*(j-1) - 4 - tmp >= 0 else 2*(j-1) - 4 - tmp
                i += 1
                m -= 1
                break
            if j > 0:
                arr.insert(2 * j + tmp, i)
            else:
                arr.insert(j + 1, i)
            i += 1
            m -= 1
            if m == 0:
                return max(d.values())
        else:
            k = 0
            tmp = 1
    return max(d.values())

# print(puzzle('input.txt'))
print(puzzle('test.txt'))