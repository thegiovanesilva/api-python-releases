from pymongo_inmemory import MongoClient
from app.repositories.delete_version_repository import DeleteVersionRepository
import pytest
from mongomock import MongoClient

client = MongoClient()
db = client["releases"]
collection = db["releases"]

@pytest.fixture(autouse=True)
def run_before_each_test():
    collection = db["releases"]
    yield collection
    
@pytest.fixture(autouse=True)
def run_after_each_test():
    collection.drop()
    yield

@pytest.fixture(autouse=True)
def run_after_all_tests():
    client.close()
    yield

def test_delete_version_without_id():
    sut = DeleteVersionRepository(db)
    with pytest.raises(Exception) as exception:
        sut.delete(None)
    assert str(exception.value) == 'ID is required'

def test_delete_version_with_valid_id():
    sut = DeleteVersionRepository(db)
    document = collection.insert_one({"version": "3.0.1", "date": '2021-01-02', "project": "project4"})
    result = sut.delete(str(document.inserted_id))
    assert result == 1