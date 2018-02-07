from tinydb import TinyDB, Query


db = TinyDB('db.json')


def insert(data):
    db.insert(data)


def clear():
    db.purge()


def read(data_uuid):
    q = Query()
    return db.search(q.uuid == data_uuid)
