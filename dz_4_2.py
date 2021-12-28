def odd_nums(x):
    i = 0
    res = []
    while i <= x:
        cnt = i
        if(cnt % 2 == 1):
            res.append(cnt)
        i+=1
    return res

print(odd_nums(15))