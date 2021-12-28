prices = [12, 11.07, 321.2, 543, 400, 127.9, 90, 567.31, 4395.12, 233.12, 5464.12]

id = 0
prices.sort()
for price in prices:
    temp = str(price).split(".")
    rub = ""
    kop = ""
    if(len(temp) != 2):
        rub = temp[0]
        kop = "00"
    else:
        rub = temp[0]
        kop = temp[1]
    prices[id] = rub + " rub " + kop + " kop"
    id += 1
newprices = reversed(prices)

for i in prices:
    print(i)

print("\nTOP 5: \n")

for i in range(5):
    print(prices[len(prices)-i-1])