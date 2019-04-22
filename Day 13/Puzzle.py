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

            # описание встреч
            elif car[3] in direct:
                return car[0][::-1]


print(puzzle('test.txt'))
print(puzzle('input.txt'))
