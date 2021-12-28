import csv
res = dict()
fio = []
hob = []
with open('users.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        fio.append(row[0] + row[1] + row[2])

with open('hobby.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        hob.append(row)

for i in range(len(fio)):
    res[fio[i]] = hob[i]
print(res)