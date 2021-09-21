import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient)
    db = myclient['Ayush']
    collection = db['mysamplecollection']
    # dictionary = {'name': 'AKS', 'marks': 50}
    # collection.insert_one(dictionary)
    mySampleList = [
        {'name': 'ABC', 'Location': 'Pune', 'marks': '35'},
        {'name': 'MNO', 'Location': 'Pune', 'marks': '45'},
        {'name': 'PQR', 'Location': 'Pune', 'marks': '55'},
        {'name': 'XYZ', 'Location': 'Pune', 'marks': '40'},
    ]
    collection.insert_many(mySampleList)