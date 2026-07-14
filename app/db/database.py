from ..core.config import supabase_database
from ..utils.short_url import create_short_url
from ..utils.datetime_json import convert_datetime_to_json
from datetime import datetime

def insert_url(url: str):
  short_url = create_short_url(url)
  date = convert_datetime_to_json(datetime.now())

  data = supabase_database.table("url-table").insert({
    "url": url,
    "short_url": short_url,
    "updated_at": date,
  }).execute()

  return data.data[0]


if __name__ == "__main__":
  results = supabase_database.table("url-table").select("*").execute()
  print(results)