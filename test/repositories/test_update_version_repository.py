from cmath import exp
from pymongo_inmemory import MongoClient
from app.repositories.update_version_repository import UpdateVersionRepository
import pytest

client = MongoClient()
db = client['releases']
collection = db['versions']

@pytest.fixture(autouse=True)
def run_before_each_test():
    collection = db["versions"]
    yield collection
@pytest.fixture(autouse=True)
def run_after_each_test():
    collection.drop()
    client.close()
    yield


def test_update_version_without_passing_id():
    sut = UpdateVersionRepository()
    with pytest.raises(Exception) as exc_info:
        sut.update_version()
        assert str(exc_info.value) == 'ID is required!'

def test_update_version_without_passing_object():
    sut = UpdateVersionRepository()
    with pytest.raises(Exception) as exc_info:
        sut.update_version("1")
        assert str(exc_info.value) == 'Data to update is required!'