from heapq import heappush, heappop


def puzzle(inp):
    # Создаем словарь букв, значения которых - кортежи с первым значением -
    # буквы, от которых зависит данная буква, второе - на которые она влияет
    # Потом с помощью доп словаря перебираем все буквы, очищая словарь
    with open(inp) as f:
        arr = f.readlines()
    d_lets = dict()
    res = ''

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

    tmp_d = {}
    tmp_k = []
    count = len(d_lets)
    while len(res) < count:
        for key, value in d_lets.items():
            if not value[0]:
                heappush(tmp_k, key)
                tmp_d[key] = value
        for key in tmp_k:
            if key in d_lets:
                del d_lets[key]
        tmp = heappop(tmp_k)
        res += tmp
        for i in tmp_d[tmp][1]:
            d_lets[i][0].discard(tmp)
        del tmp_d[tmp]

    return res


print(puzzle('test.txt'))
print(puzzle('input.txt'))