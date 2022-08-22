from app.repositories.db.db_helper import Database 
database = Database.connect()["releases"]

class LoadVersionRepository:
    def __init__(self, DB=database): 
        self.db = DB
    def load_all_versions(self):
        collection = self.db.get_collection('versions')
        versions = collection.find()
        result = []
        for version in versions:
            object = {
                'version': version['version'],
                'date': version['date'],
                'project': version['project']
            }
            result.append(object)
        return result
    def load_version_by_date(self, date):
        collection = self.db.get_collection('versions')
        versions = collection.find({"date": date})
        result = []
        for version in versions:
            object = {
                'version': version['version'],
                'date': version['date'],
                'project': version['project']
            }
            result.append(object)
            return result
    def load_version_by_project(self, project):
        collection = self.db.get_collection('versions')
        versions = collection.find({"project": project})
        result = []
        for version in versions:
            object = {
                'version': version['version'],
                'date': version['date'],
                'project': version['project']
            }
            result.append(object)
            return result
        