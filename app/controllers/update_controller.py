from app.repositories.update_version_repository import UpdateVersionRepository

class UpdateController:
    def __init__(self, request, headers, repository=UpdateVersionRepository()):
        self.repository = repository
        self.request = request
        self.headers = headers
    
    def update(self):
        
        token = self.headers["Access-Token"]
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401
        data = self.request  
        if not data or not data["id"] or not data["version"] or not data["date"] or not data["project"]:
              body = "Error"
              message = "Data is required"
              status = 400
        else:
              result = self.repository.update(data["id"],{"version": data["version"], "date": data["date"], "project": data["project"]})
              body = result
              message = None
              status = 200
      
        return {"message": message, "status" : status, "body": body}


              
              