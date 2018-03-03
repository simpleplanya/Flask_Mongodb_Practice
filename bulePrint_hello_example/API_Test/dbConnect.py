from db import get_db
db = get_db()

x = db.testData.find()
print (list(x))
