from pymongo  import Connection

if __name__ == '__main__':
    con = Connection()
    db = con.test_database
    people = db.people

