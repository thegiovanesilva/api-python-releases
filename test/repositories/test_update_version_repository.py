from pymongo_inmemory import MongoClient
from app.repositories.update_version_repository import UpdateVersionRepository
import pytest
from bson import ObjectId


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

def test_update_version_without_id():
    sut = UpdateVersionRepository(db)
    with pytest.raises(Exception) as exception:
        sut.update(None, None)
    assert str(exception.value) == 'ID is required'
def test_update_version_without_data():
    sut = UpdateVersionRepository(db)
    with pytest.raises(Exception) as exception:
        sut.update('1', None)
    assert str(exception.value) == 'Data to update is required'

def test_update_version_with_invalid_id():
    fake_data = {
        "version": "1.0.0",
        "date": '2020-01-01',
        "project": "project1"
    }
    sut = UpdateVersionRepository(db)
    with pytest.raises(Exception) as exception:
        sut.update('1', fake_data)
    assert str(exception.value) == 'Version not found'

def test_update_version_with_valid_data():
    sut = UpdateVersionRepository(db)
    data = {
        "version": "1.0.0",
        "date": '2020-01-01',
        "project": "project1"
    }
    document = collection.insert_one(data)
    new = {
       "version": "1.0.1",
       "date": "2020-01-02",
       "project": "project2"
    }
    result = sut.update(str(document.inserted_id), new)
    result2 = collection.find_one_and_update({'_id': ObjectId(str(document.inserted_id))}, {'$set': new})
    assert result['id'] == str(document.inserted_id)
    assert result['version'] == new['version']
    assert result['date'] == new['date']
    assert result['project'] == new['project']
    