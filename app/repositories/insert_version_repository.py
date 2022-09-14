from app.repositories.db.db_helper import Database
from app.utils.output_formatter import Formatter

database = Database.connect()["releases"]
class InsertVersionRepository:
  def __init__(self, DB=database):
       self.db = DB
  
  def insert_version(self, data):
      if not data:
          raise Exception('Data is required')
      collection = self.db.get_collection('releases')
      document = collection.insert_one(data)
      return str(document.inserted_id)
