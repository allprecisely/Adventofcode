import unittest

def puzzle(inp):
    # Создаем массив по правилам до нужного элемента
    arr = [3, 7, 1, 0]
    first = 0
    second = 1
    while len(arr) < inp + 10:
        new_rec = str(arr[first] + arr[second])  # Новые рецепты

        # Добавление одного или двух новых рецептов в конец
        arr.append(int(new_rec[0]))
        if len(new_rec) > 1:
            arr.append(int(new_rec[1]))

        # Вычисление новых координат с учетом возможности вылезти за пределы массива
        if arr[first] + 1 + first >= len(arr):
            first += 1 + arr[first] - len(arr)
        else:
            first += arr[first] + 1
        if arr[second] + 1 + second >= len(arr):
            second += 1 + arr[second] - len(arr)
        else:
            second += arr[second] + 1

    # Склейка нужных элементов в строку
    return ''.join(map(str, arr[inp:inp+10]))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(puzzle(5), '0124515891')
        self.assertEqual(puzzle(9), '5158916779')
        self.assertEqual(puzzle(18), '9251071085')
        self.assertEqual(puzzle(2018), '5941429882')


if __name__ == '__main__':
    print(puzzle(909441))
    unittest.main()
