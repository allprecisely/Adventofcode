import unittest


def puzzle(inp):
    # Создаем массив по правилам до нужного элемента. Но я не придумал ничего умнее подбора
    # Задачу решил, но считает минуту где-то)
    arr = [3, 7, 1, 0]
    first = 0
    second = 1
    # К сожалению подбором только...
    while len(arr) < 30000000:
        new_rec = str(arr[first] + arr[second])  # Новые рецепты

        # Добавление одного или двух новых рецептов в конец
        arr.append(int(new_rec[0]))
        if len(new_rec) > 1:
            arr.append(int(new_rec[1]))

        # Вычисление новых координат с учетом возможности вылезти за пределы массива
        if arr[first] + 1 + first >= len(arr):
            first = 1 + arr[first] - len(arr) + first
        else:
            first = arr[first] + first + 1
        if arr[second] + 1 + second >= len(arr):
            second = 1 + arr[second] - len(arr) + second
        else:
            second = arr[second] + second + 1

    # Склейка нужных элементов в строку + поиск искомой
    arr = ''.join(map(str,arr))
    return arr.index(inp)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(puzzle('0124515891'), 5)
        # Тут очень тяжелые тесты...
        # self.assertEqual(puzzle('5158916779'), 9)
        # self.assertEqual(puzzle('9251071085'), 18)
        # self.assertEqual(puzzle('5941429882'), 2018)


if __name__ == '__main__':
    print(puzzle('909441'))
    unittest.main()
