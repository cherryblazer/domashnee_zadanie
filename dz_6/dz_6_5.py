import csv
res = dict()
fio = []
hob = []

user = input("input user file")

with open(user, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        fio.append((row[0], row[1], row[2]))


hobby = input("input hobby file")

with open(hobby, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        hob.append(row)

for i in range(len(fio)):
    res[fio[i]] = hob[i]

result = input("input result file")

with open(result, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(fio)):
        writer.writerow((fio[i], hob[i]))
