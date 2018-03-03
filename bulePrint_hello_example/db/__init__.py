from pymongo  import MongoClient

if __name__ == '__main__':
    db = MongoClient(host='localhost:27017',replicaset=None)['Jq']
    con = db['testData']
    x = db.testData.find({})
    print(list(con.find()))
