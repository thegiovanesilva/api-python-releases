from pymongo_inmemory import MongoClient
from app.repositories.insert_version_repository import InsertVersionRepository
import pytest

from mongomock import MongoClient

client = MongoClient()
db = client["releases"]
collection = db["versions"]

def test_insert_version_without_data():
    sut = InsertVersionRepository(db)
    with pytest.raises(Exception) as exception:
        sut.insert_version(None)
    assert str(exception.value) == 'Data is required'

def test_insert_version_with_valid_data():
    sut = InsertVersionRepository(db)
    data = {
        "version": "1.0.0",
        "date": '2020-01-01',
        "project": "project1"
    }
    document = sut.insert_version(data)
    assert document is not None
    