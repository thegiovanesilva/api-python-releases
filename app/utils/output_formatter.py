class Formatter:
  def format(data):
    result = []
    for item in data:
      result.append({
        'id': str(item['_id']),
        'version': item['version'],
        'date': item['date'],
        'project': item['project']
      })
    return result