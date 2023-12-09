from disc_golf_app.extensions import mdb

COLLECTION = mdb.client.DiscGolf.Discs

def getAllDiscs():
    return list(COLLECTION.find({}, {'_id': False}).sort([('speed', -1), ('fade', -1), ('turn', -1)]))

def getAllBrands():
    return COLLECTION.distinct('brand')

def getSearchDiscs():
    discs = []
    for x in COLLECTION.find({}, {'name':1}):
        discs.append(x['name'])
    return discs

def getDisc(name):
    return COLLECTION.find_one({'name_lower': name}, {'_id': False})

def getRelatedDiscs(name):
    chosen_disc = getDisc(name)
    return list(COLLECTION.find({'speed': chosen_disc['speed'],
                     'turn': chosen_disc['turn'],
                     'fade': chosen_disc['fade'],
                     'name_lower': {'$ne': name}
                     },
                     {'_id': False, 'name': 1, 'distance_category': 1}))