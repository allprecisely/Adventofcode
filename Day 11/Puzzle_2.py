import unittest


def puzzle(Z, q = None, r = None):
    # Формулу так и не придумал... в итоге сложность О(n^3), считает за 2 минуты))
    power = [[0]*300 for i in range(300)]
    for y in range(300):
        for x in range(300):
            power[y][x] = ((x+10)*((x+10)*(y+0) + Z))//100%10 - 5

    res = x_max = y_max = 0
    k_max = 0
    for x in range(300):
        for y in range(300):
            tmp = power[x][y]
            for k in range(1, 300-max(x, y)):
                tmp += sum(power[x+k][y:y + k + 1])
                for k1 in range(k):
                    tmp += power[x+k1][y+k]
                if res < tmp:
                    x_max, y_max = y, x
                    res = tmp
                    k_max = k

    if q:
        return power[r][q]
    return (x_max, y_max, k_max+1)


class Test(unittest.TestCase):
    def test3(self):
        self.assertEqual(puzzle(18), (90,269,16))
        self.assertEqual(puzzle(42), (232,251,12))

print(puzzle(3463))

if __name__ == '__main__':
    unittest.main()