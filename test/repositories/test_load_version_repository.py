from pymongo_inmemory import MongoClient
from app.repositories.load_version_repository import LoadVersionRepository
import pytest

from mongomock import MongoClient

client = MongoClient()
db = client["releases"]
collection = db["versions"]

@pytest.fixture(autouse=True)
def run_before_each_test():
    collection = db["versions"]
    yield collection
@pytest.fixture(autouse=True)
def run_after_each_test():
    collection.drop()
    client.close()
    yield

def test_load_all_versions():
    sut = LoadVersionRepository(db)
    data = [
    {"version": "1.0.0", "date": '2020-01-01', "project": "project1"},
    {"version": "1.0.1", "date": '2020-01-02', "project": "project2"},
    {"version": "1.0.2", "date": '2020-01-03', "project": "project3"},
    {"version": "1.0.3", "date": '2020-01-04', "project": "project4"}
    ]
    
    mocked_data = []
    for item in data:
        object = {
            'version': item['version'],
            'date': item['date'],
            'project': item['project']
        }
        mocked_data.append(object)
    collection.insert_many(data)
    result = sut.load_all_versions()        
    assert result == mocked_data

def test_load_all_versions_empty():
    sut = LoadVersionRepository(db)
    result = sut.load_all_versions()        
    assert result == []

def test_load_version_by_date_inexistent():
    sut = LoadVersionRepository(db)
    result = sut.load_version_by_date('2020-01-01')        
    assert result == None

def test_load_version_with_valid_dates():
    sut = LoadVersionRepository(db)
    data = [
    {"version": "1.0.0", "date": '2020-01-01', "project": "project1"},
    {"version": "1.0.1", "date": '2020-01-02', "project": "project2"},
    {"version": "1.0.2", "date": '2020-01-03', "project": "project3"},
    {"version": "1.0.3", "date": '2020-01-04', "project": "project4"}
    ]    
    collection.insert_many(data)
    expected_data = [{"version": "1.0.0", "date": '2020-01-01', "project": "project1"}]
    
    result = sut.load_version_by_date('2020-01-01')        
    assert result == expected_data

def test_load_version_by_project_inexistent():
    sut = LoadVersionRepository(db)
    result = sut.load_version_by_project('inexistent_project')        
    assert result == None

def test_load_version_by_project_with_an_existent_project():
    sut = LoadVersionRepository(db)
    data = [
    {"version": "1.0.0", "date": '2020-01-01', "project": "project1"},
    {"version": "1.0.1", "date": '2020-01-02', "project": "project2"},
    {"version": "1.0.2", "date": '2020-01-03', "project": "project3"},
    {"version": "1.0.3", "date": '2020-01-04', "project": "project4"}
    ]    
    collection.insert_many(data)
    expected_data = [{"version": "1.0.0", "date": '2020-01-01', "project": "project1"}]
    result = sut.load_version_by_project('project1')
    assert result == expected_data    