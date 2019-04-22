def puzzle(inp):
    # Идея в том, чтобы не проходить каждый раз поле, а запомнить все машинки и двигать их
    # Вроде очень прямолинейно решил, но по другому не знаю как..
    with open(inp) as f:
        arr = f.readlines()
    cars = []
    field = [list(i) for i in arr]  # Массив поле
    direct = ['>', 'v', '<', '^']  # Смена направлений на перекрестках
    turn1 = {'<': '^', '^': '<', '>': 'v', 'v': '>'}  # Смена направления на повороте /
    turn2 = {'<': 'v', 'v': '<', '>': '^', '^': '>'}  # Смена направления на повороте \

    # Поиск всех машин, и формирование массива
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] in 'v^':
                cars.append([[y,x], arr[y][x], 1, '|'])
            elif field[y][x] in '<>':
                cars.append([[y,x], arr[y][x], 1, '-'])

    #
    while len(cars) != 1:
        # так как обновляются координаты машин, необходимо их сортировать для правильно последовательнсти
        cars.sort()
        for car in cars:
            if car == [[0]]:
                continue
            # описание движения
            if car[1] == '>':
                field[car[0][0]][car[0][1]] = car[3]
                car[3] = field[car[0][0]][car[0][1] + 1]
                field[car[0][0]][car[0][1] + 1] = '>'
                car[0][1] += 1
            elif car[1] == '<':
                field[car[0][0]][car[0][1]] = car[3]
                car[3] = field[car[0][0]][car[0][1] - 1]
                field[car[0][0]][car[0][1] - 1] = '<'
                car[0][1] -= 1
            elif car[1] == '^':
                field[car[0][0]][car[0][1]] = car[3]
                car[3] = field[car[0][0] - 1][car[0][1]]
                field[car[0][0] - 1][car[0][1]] = '^'
                car[0][0] -= 1
            elif car[1] == 'v':
                field[car[0][0]][car[0][1]] = car[3]
                car[3] = field[car[0][0] + 1][car[0][1]]
                field[car[0][0] + 1][car[0][1]] = 'v'
                car[0][0] += 1

            # описание перекрестков и поворотов
            if car[3] == '+':
                if car[2] == 1:
                    car[1] = direct[direct.index(car[1])-1]
                elif car[2] == 3:
                    car[1] = direct[::-1][direct[::-1].index(car[1])-1]
                car[2] = car[2] + 1 if car[2] != 3 else 1
            elif car[3] == "\\":
                car[1] = turn1[car[1]]
            elif car[3] == "/":
                car[1] = turn2[car[1]]

            # описание встреч (для первого решения достаточно сделать брейк для 1 вхождения)
            elif car[3] in direct:
                for i in cars:
                    if i == [[0]]:
                        continue
                    if i[0] == car[0] and i != car:
                        field[car[0][0]][car[0][1]] = i[3]
                        cars[cars.index(i)] = [[0]]
                        cars[cars.index(car)] = [[0]]
                        break

        # тут я устал думать и придумал удаление машин таким образом
        tmp = []
        for i in range(len(cars)):
            if cars[i] != [[0]]:
                tmp.append(cars[i])
        cars = tmp

    return cars[0][0][::-1]


print(puzzle('test2.txt'))
print(puzzle('input.txt'))