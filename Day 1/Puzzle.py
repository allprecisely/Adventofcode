def puzzle(inp):
    sum = 0
    arr = set()
    with open(inp) as f:
        strings = f.readlines()
    while True:
        for i in strings:
            sum += int(i)
            if sum in arr:
                return sum
            arr.add(sum)


print(puzzle('input.txt'))