# Идея в обходе в ширину. Как я шел к этому алгоритму в папке
# Недочеты: не понимаю, почему количество раундов отличается...

# модуль нужен для BFS
from collections import deque

def f(file):
    conter = {'G': 'E', 'E': 'G'}  # для одного цикла for

    with open(file) as f:
        strings = f.readlines()
    arr1 = [list(i.replace('\n', '')) for i in strings]

    # Перепись населения в начале игры
    def find_everybody(arr):
        creatures = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] in 'EG':  # эльфы, гоблины... важно присутствие на поле, а не кто есть кто
                    creatures.append({'pos': (i, j), 'HP': 200, 'race': arr[i][j]})
        return creatures

    # Обновление поля после каждого хода
    def graph_creation(unit):
        graph = {}

        # Создание вершин графа
        for i in range(len(arr1)):
            for j in range(len(arr1[0])):
                if arr1[i][j] in '.GE':
                    graph[i, j] = set()

        # Создание ребер графа
        for i in range(1, len(arr1) - 1):
            for j in range(1, len(arr1[0]) - 1):
                if arr1[i][j] != '#':
                    for k in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                        if arr1[k[0]][k[1]] == '.' or arr1[k[0]][k[1]] == unit:
                            graph[i, j].add(k)

        return graph

    # Собственно BFS
    def find_way(graph, start, race):
        deq = deque()
        deq.append(start)
        W = {start: None}
        way = []

        while len(deq) > 0:
            tmp = deq.popleft()
            if arr1[tmp[0]][tmp[1]] == race:  # как только находим ближайшего противника, возвращаем путь
                break
            for i in sorted(graph[tmp]):
                if i not in W:
                    W[i] = tmp
                    deq.append(i)
        else:  # если путей нет, то отмечаем это
            return -1

        # рисуем траекторию движения
        while tmp != start:
            way += [tmp]
            tmp = W.get(tmp, None)

        return way

    # если противники рядом, то выбираем самого слабого и атакуем его
    def find_enemy(unit, enemy):
        i, j = unit['pos'][0], unit['pos'][1]
        enemies = []
        for k in (i-1,j), (i, j-1), (i, j+1), (i+1,j):  # проверка всех клеток рядом
            for u in range(len(units)):
                if units[u]['pos'] == k and units[u]['race'] == enemy:
                    enemies.append((units[u]['HP'], u))  # перечисляем всех противников
                    break
        aim = min(enemies)[1]  # выбираем самого слабого
        units[aim]['HP'] -= 3
        if units[aim]['HP'] <= 0:  # когда противник умирает, он отправляется на кладбище (0,0)
            units[aim]['HP'] = 0  # у меня идет перебор по всем персонажам. А менять список при переборе нельзя
            arr1[units[aim]['pos'][0]][units[aim]['pos'][1]] = '.'
            units[aim]['pos'] = (0,0)

    units = find_everybody(arr1)
    counter = len(units)  # так как я шел через кладбище и не разделял персонажей по расам, то у меня
    # выход реализован через проверку, что ВСЕ персонажи или на кладбище или не могут сходить

    q = 0  # раунды
    # здесь мы каждый раунд обновляем всех персонажей поочереди
    while counter:

        # это для прорисовки поля после каждого хода
        # for i1 in range(len(arr1)):
        #     print()
        #     for j1 in range(len(arr1[0])):
        #         print(arr1[i1][j1], end=' ')
        # print()

        counter = len(units)  # после каждого хода обновляем счетчик (если он не ноль конечно)

        units.sort(key=lambda unit: unit['pos'])  # инициатива меняется в зависимости от положения персонажа
        # именно из-за инициативы я решил не разделять персонажей на злых и добрых
        # если их разделять, то придется делать много лишних движений, чтобы определить инициативу
        # "инициатива" - в играх это очередность хода

        q += 1

        for i in range(len(units)):  # несмторя на то, что я пребираю не персонажей, а диапазон
            # я все равно не могу просто щелчком пальцев испарять персонажей - иначе вылезу за границы списка персов
            # и именно из-за этого пришлось реализовать кладбище
            # да, из них потом могут получится белые ходоки, но это будет совсем другая история

            if units[i]['HP'] <= 0:  # если перс на кладбище, отмечаем это в счетчике
                counter -= 1
                continue

            graph = graph_creation(conter[units[i]['race']])  # заново отрисовываем граф для перса
            way = find_way(graph, units[i]['pos'], conter[units[i]['race']])  # и находим путь до ближайшего противника
            # да, много лишних телодвижений - но у меня уже голова кипела, когда дошел до сюда

            if way == -1:  # выше мы отметили, когда путей нет. Отметим это для счетчика
                counter -= 1
                continue

            if len(way) <= 1:  # если стоим рядом, то атакуем
                find_enemy(units[i], conter[units[i]['race']])
                continue

            # если не рядом, то топаем к противнику
            arr1[units[i]['pos'][0]][units[i]['pos'][1]] = '.'
            arr1[way[-1][0]][way[-1][1]] = units[i]['race']
            units[i]['pos'] = way.pop()

            # и если в конце шага мы к нему подошли, то сразу атакуем
            if len(way) == 1:
                find_enemy(units[i], conter[units[i]['race']])

    # отображение ХП каждого персонажа в конце
    # for u in units:
    #     print(u)

    # подсчет общего хп в конце
    res = 0
    for i in units:
        res += i['HP']

    # отображени результата
    return (q-2)*res, q-2, res

print(f('test1.txt'), 27730)
print(f('test2.txt'), 36334)
print(f('test3.txt'), 39514)
print(f('test4.txt'), 27755)
print(f('test5.txt'), 28944)
print(f('test6.txt'), 18740)
print(f('input.txt'), 191216)