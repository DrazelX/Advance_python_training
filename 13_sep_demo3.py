import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient)
    allDatabases = myclient.list_database_names()
    print(allDatabases)
    col = myclient['Ayush']
    print(col.list_collection_names())