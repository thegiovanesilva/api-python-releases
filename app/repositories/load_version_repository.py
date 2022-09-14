from app.repositories.db.db_helper import Database
from app.utils.output_formatter import Formatter
database = Database.connect()["releases"]

class LoadVersionRepository:
    def __init__(self, DB=database): 
        self.db = DB
    def load_all_versions(self):
        collection = self.db.get_collection('releases')
        versions = collection.find()            
        return Formatter.format(versions)

    def load_version_by_date(self, date):
        collection = self.db.get_collection('releases')
        versions = collection.find({"date": date})
        return Formatter.format(versions)

    def load_version_by_project(self, project):
        collection = self.db.get_collection('releases')
        versions = collection.find({"project": project})
        return Formatter.format(versions)
        