from importlib.resources import path
from sys import path

from app.repositories.db.db_helper import Database
from app.repositories.load_version_repository import LoadVersionRepository

pytest_plugins = ['pytester']  # Entire contents of file!

# path.append(app)