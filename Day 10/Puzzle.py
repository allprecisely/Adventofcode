import re
import unittest

def puzzle(inp):
    # Идея в обновлении координат до тех пор, пока разброс точек не будет минимальным
    with open(inp) as f:
        strings = f.readlines()
    arr = [[] for i in range(len(strings))]

    x, y = [0] * len(arr), [0] * len(arr)
    for i in range(len(strings)):
        string = re.findall(r'-?\d+', strings[i])
        arr[i] = [int(x) for x in string]
        x[i] = arr[i][0]
        y[i] = arr[i][1]

    t = -1
    while True:
        t += 1
        tmp_x = max(x) - min(x)
        tmp_y = max(y) - min(y)

        for i in range(len(arr)):
            arr[i][0] += arr[i][2]
            arr[i][1] += arr[i][3]
            x[i] = arr[i][0]
            y[i] = arr[i][1]

        if tmp_x < max(x) - min(x) or tmp_y < max(y) - min(y):
            for i in range(len(arr)):
                arr[i][0] -= arr[i][2]
                arr[i][1] -= arr[i][3]
            break

    tmp_arr = [['.' for i in range(min(x), max(x) + 1)] for j in range(min(y), max(y) + 1)]

    for i in range(len(arr)):
        tmp_arr[arr[i][1]-min(y)][arr[i][0]-min(x)] = '#'

    with open('pict.txt', 'a') as f:
        for i in range(len(tmp_arr)):
            f.write(''.join(tmp_arr[i]) + '\n')

    return tmp_arr, t

class test(unittest.TestCase):
    def test_time(self):
        ans = puzzle('test.txt')
        self.assertEqual(ans[1], 3)

print(puzzle('input.txt')[1])
if __name__ == '__main__':
    unittest.main()