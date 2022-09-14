from bson import ObjectId
from app.repositories.db.db_helper import Database
database = Database.connect()["releases"]
class UpdateVersionRepository:
    def __init__(self, DB=database):
        self.db = DB
    def update(self, id, data):
        if not id:
            raise Exception('ID is required')
        if not data:
            raise Exception('Data to update is required')
        
        collection = self.db.get_collection('releases')
        try:
            collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': data}) 
            return {
                'id': id,
                'version': data['version'],
                'date': data['date'],
                'project': data['project']
                }
        except:
            raise Exception('Version not found')
        