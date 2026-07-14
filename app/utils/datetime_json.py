import json

def convert_datetime_to_json(datetime):
  json_datetime = json.dumps(datetime.now(), default=str)
  return json_datetime

if __name__ == "__main__":
  from datetime import datetime

  json_datetime = convert_datetime_to_json(datetime.now())
  print(json_datetime)