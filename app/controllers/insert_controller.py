from app.repositories.insert_version_repository import InsertVersionRepository

class InsertController:
    def __init__(self, request, headers, repository=InsertVersionRepository()):
        self.repository = repository
        self.request = request
        self.headers = headers
    
    def insert(self):
        token = self.headers["Access-Token"] == "123456"
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401
        data = self.request  
        if not data or not data["version"] or not data["date"] or not data["project"]:
              body = "Error"
              message = "Data is required"
              status = 400
        else:
              result = self.repository.insert_version(data)
              body = result
              message = None
              status = 200
      
        return {"message": message, "status" : status, "body": body}