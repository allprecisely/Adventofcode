def puzzle(inp, gen):
    # Засовываем паттерны в словарь, и проверяем каждый символ и 2 вокруг с этим паттерном
    # 42 нужно, чтобы посчитать на сколько сместилось решение
    # Идея второй части в том, что не хватит памяти посчитать на таких столетиях. Зато на 20 столетии...
    # можно увидеть зависимость, которая к 100му охватывает весь промежуток
    with open(inp) as f:
        arr = f.readlines()
    dct = {arr[i][0:5]:arr[i][9] for i in range(2, len(arr))}
    string = '.'*(2*gen+2) + arr[0][15:-1]
    res = 0

    for time in range(gen):
        string = string + '.'*(5 - (len(string) - string.rindex('#')))
        tmp = []
        for i in range(2,len(string)-2):
            tmp.append(dct.get(string[i-2:i+3], '.'))
        string = ''.join(tmp)

    for i in range(len(string)):
        if string[i] == '#':
            res += i - 2
    return res

print('First part: ', puzzle('input.txt', 20))
print('Second part: ', puzzle('input.txt', 100) + (50000000000-100)*78)
print('Test: ', puzzle('test.txt', 20))