from pymongo import MongoClient

def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll


def getLocation(emp):
    location = []
    longitude = emp['latitud']
    latitude = emp['longitud']
    loc = {
        'type':'Point',
        'coordinates':[float(longitude), float(latitude)]
    }
    location.append(loc)
    return location