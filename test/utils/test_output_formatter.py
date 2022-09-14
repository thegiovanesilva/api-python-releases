from app.utils.output_formatter import Formatter

def test_format_with_an_empty_data():
    result = Formatter.format([])
    assert result == []

def test_format_with_a_valid_data():
    data = [{
        '_id': '123',
        'version': '1.0.0',
        'date': '2020-01-01',
        'project': 'project'
    }]
    result = Formatter.format(data)
    assert result[0]['id'] == data[0]['_id']
    assert result[0]['version'] == data[0]['version']
    assert result[0]['date'] == data[0]['date']
    assert result[0]['project'] == data[0]['project']