def puzzle(inp):
    with open(inp) as f:
        string = f.read()
    res = len(string)
    for i in range(97,123):
        string1 = string.replace(chr(i), '').replace(chr(i).upper(), '')
        arr = ['0', string1[0]]
        for i in range(1, len(string1)):
            if arr[-1].lower() == string1[i].lower() and arr[-1] != string1[i]:
                arr.pop()
            else:
                arr.append(string1[i])
        res = res if res < len(arr) - 1 else len(arr) - 1
    return(res)


print(puzzle('input.txt'))