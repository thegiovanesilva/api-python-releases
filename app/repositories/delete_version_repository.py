from app.repositories.db.db_helper import Database
from bson import ObjectId

database = Database.connect()["releases"]
class DeleteVersionRepository:
    def __init__(self, DB=database):
        self.db = DB

    def delete(self, id):
        if not id:
            raise Exception('ID is required')
        collection = self.db.get_collection('releases')
        document = collection.delete_one({'_id': ObjectId(id)})
        return document.deleted_count