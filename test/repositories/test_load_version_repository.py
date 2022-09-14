from pymongo_inmemory import MongoClient
from app.repositories.load_version_repository import LoadVersionRepository
import pytest

from mongomock import MongoClient

client = MongoClient()
db = client["releases"]
collection = db["versions"]

data = [
    {"version": "1.0.0", "date": '2020-01-01', "project": "project1"},
    {"version": "1.0.1", "date": '2020-01-02', "project": "project2"},
    {"version": "1.0.2", "date": '2020-01-03', "project": "project3"},
    {"version": "1.0.3", "date": '2020-01-04', "project": "project4"}
]

@pytest.fixture(autouse=True)
def run_before_each_test():
    collection = db["versions"]
    yield collection
    
@pytest.fixture(autouse=True)
def run_after_each_test():
    collection.drop()
    yield

@pytest.fixture(autouse=True)
def run_after_all_tests():
    client.close()
    yield

def test_load_all_versions():
    sut = LoadVersionRepository(db)
    mocked_data = []
    for item in data:
        object = {
            'version': item['version'],
            'date': item['date'],
            'project': item['project']
        }
        collection.insert_one(object)
        mocked_data.append(object)
    
    result = sut.load_all_versions()        
    for index, item in enumerate(result):
        assert item['id'] == str(mocked_data[index]['_id'])
        assert item['version'] == mocked_data[index]['version']
        assert item['date'] == mocked_data[index]['date']
        assert item['project'] == mocked_data[index]['project']

def test_load_all_versions_empty():
    sut = LoadVersionRepository(db)
    result = sut.load_all_versions()        
    assert result == []

def test_load_version_by_date_inexistent():
    sut = LoadVersionRepository(db)
    result = sut.load_version_by_date('2020-01-01')        
    assert result == []

def test_load_version_with_valid_dates():
    sut = LoadVersionRepository(db)
    for item in data:
        object = {
            'version': item['version'],
            'date': item['date'],
            'project': item['project']
        }
        collection.insert_one(object)
        
    expected_data = collection.find({"date": '2020-01-01'})
    result = sut.load_version_by_date('2020-01-01')
            
    for index, item in enumerate(result):
        assert item['id'] == str(expected_data[index]['_id'])
        assert item['version'] == expected_data[index]['version']
        assert item['date'] == expected_data[index]['date']
        assert item['project'] == expected_data[index]['project']

def test_load_version_by_project_inexistent():
    sut = LoadVersionRepository(db)
    result = sut.load_version_by_project('inexistent_project')        
    assert result == []

def test_load_version_by_project_with_an_existent_project():
    sut = LoadVersionRepository(db)
    mocked_data = []
    for item in data:
        object = {
            'version': item['version'],
            'date': item['date'],
            'project': item['project']
        }
        collection.insert_one(object)
        mocked_data.append(object)
    expected_data = collection.find({"date": '2020-01-01'})
    result = sut.load_version_by_project('project1')
    for index, item in enumerate(result):
        assert item['id'] == str(expected_data[index]['_id'])
        assert item['version'] == expected_data[index]['version']
        assert item['date'] == expected_data[index]['date']
        assert item['project'] == expected_data[index]['project']