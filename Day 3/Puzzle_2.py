import re

def puzzle(inp):
    with open(inp) as f:
        arr = f.readlines()
    pat = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    suit = [['']*1000 for i in range(1000)]
    st = set()
    for i in arr:
        data = pat.search(i)
        st.add(data.group(1))
        for j in range(int(data.group(2)), int(data.group(2))+int(data.group(4))):
            for k in range(int(data.group(3)), int(data.group(3))+int(data.group(5))):
                if not suit[j][k]:
                    suit[j][k] = data.group(1)
                elif suit[j][k]:
                    st.discard(suit[j][k])
                    st.discard(data.group(1))
    return st.pop()

print(puzzle('input.txt'))