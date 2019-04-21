import unittest


def puzzle(Z, q = None, r = None):
    # идея в подсчете сначала всех мощностей и потом просто подсчете квадратов 3х3
    power = [[0]*300 for i in range(300)]
    for y in range(300):
        for x in range(300):
            power[y][x] = ((x+10)*((x+10)*(y+0) + Z))//100%10 - 5

    res = x_max = y_max = 0
    for y in range(297):
        for x in range(297):
            tmp = sum(power[y][x:x+3]) + sum(power[y+1][x:x+3]) + sum(power[y+2][x:x+3])
            if res < tmp:
                x_max, y_max = x, y
                res = tmp

    if q:
        return power[r][q]
    return (x_max, y_max)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(puzzle(57,122,79), -5)
        self.assertEqual(puzzle(39,217,196), 0)
        self.assertEqual(puzzle(71,101,153), 4)

    def test2(self):
        self.assertEqual(puzzle(18), (33,45))
        self.assertEqual(puzzle(42), (21,61))

print(puzzle(3463))

if __name__ == '__main__':
    unittest.main()