from pymongo  import MongoClient
from conf import dbConfig
def get_db():
    db = MongoClient(host='localhost:27017',replicaset=None)['Jq']
    return db
