from pymongo import MongoClient
import os

class Database:
    def __init__(self):
        try:
            self.username = os.environ['DB_USERNAME']
            self.password = os.environ['DB_PASSWORD']
            self.host = os.environ['DB_HOST']
            self.port = os.environ['DB_PORT']
            self.db_name = os.environ['DB_NAME']
        except:
            self.username = 'root'
            self.password = 'password'
            self.host = 'localhost'
            self.port = '27017'
            self.db_name = 'releases'
    
    def get_database(self):
        connection_string = f"mongodb://{self.host}:{self.port}/{self.db_name}"
        client = MongoClient(connection_string)
        return client[self.db_name]
    
    def get_collection(self, collection_name):
        return self.get_database()[collection_name]

    def disconnect(self):
        self.get_database().close()


