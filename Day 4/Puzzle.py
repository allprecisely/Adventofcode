import re

def puzzle(inp):
    with open(inp) as f:
        arr = f.readlines()
    pat = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    


print(puzzle('input.txt'))