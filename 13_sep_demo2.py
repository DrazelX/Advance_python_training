import pymongo
if __name__ == "__main__":
    print("welcome to pymongo")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient)
    db = myclient['Ayush']
    collection = db['mysamplecollection']
    # one = collection.find_one({'name': 'XYZ'})
    # print(one)
    allDocs = collection.find({'name': 'XYZ'}, {'name':0, '_id':0}).limit(1)
    print(allDocs.count())
    for item in allDocs:
        print(item)