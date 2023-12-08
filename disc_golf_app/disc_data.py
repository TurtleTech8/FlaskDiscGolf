from disc_golf_app.extensions import mdb

COLLECTION = mdb.client.DiscGolf.Discs

class Disc:
    def __init__(self, brand, speed, turn, fade, glide, name, purchase_url, data_picture, distance_category):
        self.brand = brand
        self.speed = speed
        self.turn = turn
        self.fade = fade
        self.glide = glide
        self.name = name
        self.purchase_url = purchase_url
        self.data_picture = data_picture
        self.distance_category = distance_category

    def __init__(self, discBSON):
        self.brand = discBSON['brand']
        self.speed = discBSON['speed']
        self.turn = discBSON['turn']
        self.fade = discBSON['fade']
        self.glide = discBSON['glide']
        self.name = discBSON['name']
        self.purchase_url = discBSON['purchase_url']
        self.data_picture = discBSON['data_picture']
        self.distance_category = discBSON['distance_category']
    
    def __repr__(self):
        return f'{self.distance_category}: {self.brand} {self.name}'

    def __str__(self):
        return f'{self.distance_category}: {self.brand} {self.name}'

def getAllDiscs():
    # discs = []
    # for x in COLLECTION.find({}, {'_id': False}).sort([('speed', -1), ('fade', -1), ('turn', -1)]):
    #     discs.append(Disc(x).__dict__)
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