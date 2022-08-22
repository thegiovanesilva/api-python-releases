from pymongo import MongoClient
import os

class Database:
    def connect():
        # user = os.environ['DB_USERNAME']
        # password = os.environ['DB_PASSWORD']
        host ='localhost' # os.environ['DB_HOST']
        port = '27017' #os.environ['DB_PORT']
        db_name = 'releases' #os.environ['DB_NAME']
        connection_string = f"mongodb://{host}:{port}/{db_name}"
        client = MongoClient(connection_string)
        return client
