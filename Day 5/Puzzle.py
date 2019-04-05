def puzzle(inp):
    with open(inp) as f:
        string = f.read()
    arr = ['0', string[0]]
    for i in range(1, len(string)):
        if arr[-1].lower() == string[i].lower() and arr[-1] != string[i]:
            arr.pop()
        else:
            arr.append(string[i])
    return(len(arr) - 1)



print(puzzle('input.txt'))