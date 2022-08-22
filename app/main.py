from app.app import App

from app.repositories.load_version_repository import LoadVersionRepository

app = App().get_app()

@app.get("/")
def read_root():
    l = LoadVersionRepository()
    ver = l.load_all_versions()
    return (ver)