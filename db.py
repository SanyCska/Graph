from tinydb import TinyDB, Query


db = TinyDB('db.json')


def insert(data):
    db.insert(data)


def clear():
    db.purge()


def read(data_uuid):
    q = Query()
    return db.search(q.uuid == data_uuid)


def graphs():
    graphs_info = []
    for graph in db.all():
        graphs_info.append({'name': graph['name'], 'timestamp': graph['timestamp'], 'uuid': graph['uuid']})
    return graphs_info
