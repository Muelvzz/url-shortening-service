import json

def convert_datetime_to_json(datetime):
  json_datetime = json.dumps(datetime.now(), default=str)
  return json_datetime