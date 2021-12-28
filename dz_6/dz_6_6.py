sales = list(map(int, input("Enter sales separated by commas: ").split()))

query = list(map(int, input("Input your query: ").split()))
if(len(query) == 1):
    i = query[0]
    i-=1
    while(i <= len(sales)-1):
        print(sales[i])
        i+=1
else:
    for i in range(query[0], query[1]):
        print(sales[i])

