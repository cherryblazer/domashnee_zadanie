def odd_nums(x):
    i = 0
    while i <= x:
        cnt = i
        if(cnt % 2 == 1):
            yield cnt
        i+=1
odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
