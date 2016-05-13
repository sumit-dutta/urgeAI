import pymongo

from pymongo import MongoClient


client = MongoClient('54.210.10.34', 27017)
db = client.looksmashdb
flipkart = db.flipkart_data


def getColumnValues(client, dbName, collectionName, columnName):
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({}, {columnName:1, "_id":0})
    values = []
    for doc in result:
        if columnName in doc.keys():
            values.append(doc[columnName])
    return list(set(values))




def printColVals(columnName):
    print columnName
    print "flipkart",getColumnValues(client, "looksmashdb", "flipkart_data", columnName)
    print "jabong",getColumnValues(client, "looksmashdb", "jabong_data", columnName)
    print "snapdeal",getColumnValues(client, "looksmashdb", "snapdeal_data", columnName)


printColVals("Style")
printColVals("Sub_category")
printColVals("Sex")
printColVals("Fabric")
printColVals("Type")