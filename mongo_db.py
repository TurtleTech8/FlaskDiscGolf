from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDB:
    uri = "mongodb+srv://November:RandomCocoa24@cluster0.fgs9tdn.mongodb.net/?retryWrites=true&w=majority"
    def __init__(self):
        self.client = None
        
    def init_app(self):
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))