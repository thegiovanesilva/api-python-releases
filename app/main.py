from fastapi.responses import JSONResponse
from fastapi import Request

from app.app_config import App

from app.controllers.update_controller import UpdateController
from app.controllers.insert_controller import InsertController
from app.controllers.get_controller import GetController
from app.controllers.delete_controller import DeleteController
from app.entities.release import Release

app = App().get_app()

@app.get("/")
def read_root():
    return "It's working!, api-releases"

@app.get("/version/")
async def load_versions(request: Request):
    req = await request.json()
    body = GetController(req, request._headers).load_all()
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})

@app.put("/version/")
async def edit_version(request: Request, release: Release):
    req = await request.json()
    body = UpdateController(req, request._headers).update()
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})
     
@app.post("/version/")
async def create_version(request: Request, release: Release):
    req = await request.json()
    body = InsertController(req, request._headers).insert()
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})

@app.delete("/version/")
async def delete_version(request: Request):
    req = await request.json()
    body = DeleteController(req, request._headers).delete_version(req["id"])
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})


@app.post("/version/load-project")
async def load_versions_by_project(request: Request):
    req = await request.json()
    body = GetController(req, request._headers).load_by_project(req["project"])
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})

@app.post("/version/load-date")
async def load_versions_by_date(request: Request):
    req = await request.json()
    body = GetController(req, request._headers).load_by_date(req["date"])
    return JSONResponse(status_code=body["status"], content={"message": body["message"], "body": body["body"]})

