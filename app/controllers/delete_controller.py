from app.repositories.delete_version_repository import DeleteVersionRepository

class DeleteController:
    def __init__(self, request, headers, repository=DeleteVersionRepository()):
        self.repository = repository
        self.request = request
        self.headers = headers
    
    def delete_version(self, id):
        token = self.headers["Access-Token"] == "123456"
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401
        if not id:
              body = "Error"
              message = "Id is required"
              status = 400
        else:
              result = self.repository.delete(id)
              body = result
              message = None
              status = 200
      
        return {"message": message, "status" : status, "body": body} 
