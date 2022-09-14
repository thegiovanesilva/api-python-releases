from app.repositories.load_version_repository import LoadVersionRepository

class GetController:
    def __init__(self, request, headers, repository=LoadVersionRepository()):
        self.repository = repository
        self.request = request
        self.headers = headers
    
    def load_all(self):
        token = self.headers["Access-Token"]
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401
        else:
            result = self.repository.load_all_versions()
            body = result
            message = None
            status = 200
        return {"message": message, "status" : status, "body": body}

    def load_by_project(self, project):
        token = self.headers["Access-Token"] == "123456"
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401  
        if not project:
              body = "Error"
              message = "Project is required"
              status = 400
        else:
              result = self.repository.load_version_by_project(project)
              body = result
              message = None
              status = 200
        return {"message": message, "status" : status, "body": body}
      
    def load_by_date(self, date):
        token = self.headers["Access-Token"] == "123456"
        if token != "123456":
            body = "Unauthorized"
            message = "Unauthorized"
            status = 401
        if not date:
              body = "Error"
              message = "Date is required"
              status = 400
        else:
              result = self.repository.load_version_by_date(date)
              body = result
              message = None
              status = 200
        return {"message": message, "status" : status, "body": body}