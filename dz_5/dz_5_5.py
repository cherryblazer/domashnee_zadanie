def solve(src:list):
    res = {}
    resd = []
    for i in src:
        res[i] = src.count(i)
    for i in src:
        if res[i] == 1:
            resd.append(i)
    return resd
print(solve([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))