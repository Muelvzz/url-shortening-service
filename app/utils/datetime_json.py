import json

def convert_datetime_to_json(datetime):
  if not datetime:
    raise ValueError("The provided datetime is None.")

  json_datetime = json.dumps(datetime.now(), default=str)
  return json_datetime