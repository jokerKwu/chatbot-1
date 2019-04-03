import pymongo
import csv

connection = pymongo.MongoClient("localhost", 27017)
db = connection.testDB


db.drop_collection("Slot1")
db.drop_collection("Slot2")
db.drop_collection("Slot3")
db.drop_collection("Si")
db.drop_collection("Gu")
db.drop_collection("Ro")
db.drop_collection("Dong")
db.drop_collection("Data")

co = db.Slot1
f = open('slot1.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    for num in range(len(line)):
        if num % 2 == 0:
            data[line[num]] = line[num+1]
    co.insert(data)
f.close()

co = db.Slot2
f = open('slot2.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    for num in range(len(line)):
        if num % 2 == 0:
            data[line[num]] = line[num+1]
    co.insert(data)
f.close()

co = db.Slot3
f = open('slot3.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    for num in range(len(line)):
        if num % 2 == 0:
            data[line[num]] = line[num+1]
    co.insert(data)
f.close()


co = db.Si
f = open('Si.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    data[line[0]] = line[1]
    co.insert(data)
f.close()


co = db.Gu
f = open('Gu.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    data[line[0]] = line[1]
    co.insert(data)
f.close()

co = db.Dong
f = open('Dong.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    data[line[0]] = line[1]
    co.insert(data)
f.close()

co = db.Ro
f = open('Ro.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    data[line[0]] = line[1]
    co.insert(data)
f.close()


for i in range(1, 4):
    collectionName = "Slot" + str(i)
    co = db[collectionName]
    db.drop_collection(collectionName)
    f = open('slot'+str(i)+'.csv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f)
    for line in rdr:
        data = {}
        for num in range(len(line)):
            if num % 2 == 0:
                data[line[num]] = line[num + 1]
        co.insert(data)
    f.close()

db.drop_collection("Data")

co = db.Data
f = open('data.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    data = {}
    for num in range(len(line)):
        if num % 2 == 0:
            data[line[num]] = line[num+1]
    co.insert(data)
f.close()

