from collections import deque

def puzzle(inp):
    # Честно украдено с форума. Решение действительно очень хорошее, и намного понятнее, чем мое
    # первоначальное... идея в структуре Очередь... (я слышал о ней, но не знал, как применить)
    with open(inp) as f:
        string = f.read()
        string = string.split()
    p, m = int(string[0]), int(string[6])
    arr = deque()
    elfs = [0]*p
    for i in range(m+1):
        if i%23 == 0 and i != 0:
            arr.rotate(7)
            elfs[i%p] += i + arr.pop()
            arr.rotate(-1)
        else:
            arr.rotate(-1)
            arr.append(i)
    return max(elfs)

print(puzzle('input.txt'))
print(puzzle('test.txt'))