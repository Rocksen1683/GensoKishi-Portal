import csv 
import json

jsonDict = {}

with open("gensokishi\\assets\gensokishi-alloc-100.csv","r") as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        jsonDict[row[0]] = row[1]
    print(jsonDict)

with open("gensokishi\\assets\gensokishi-alloc.json","w") as jsonfile:
    json.dump(jsonDict,jsonfile)

