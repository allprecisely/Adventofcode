import re

def puzzle(inp):
    sum = 0
    with open(inp) as f:
        arr = f.readlines()
    pat = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    suit = [[' ']*1000 for i in range(1000)]
    for i in range(len(arr)):
        data = pat.search(arr[i])
        for j in range(int(data.group(2)), int(data.group(2))+int(data.group(4))):
            for k in range(int(data.group(3)), int(data.group(3))+int(data.group(5))):
                if suit[j][k] == ' ':
                    suit[j][k] = 'O'
                elif suit[j][k] == 'O':
                    sum += 1
                    suit[j][k] = 'X'
    suit = [''.join(i) for i in suit]
    with open('suit.txt', 'w') as f:
        f.write('\n'.join(suit))
    return sum


print(puzzle('input.txt'))