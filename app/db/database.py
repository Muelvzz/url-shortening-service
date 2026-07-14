from ..core.config import supabase_database
from ..utils.short_code import generate_short_code
from ..utils.datetime_json import convert_datetime_to_json
from datetime import datetime

def insert_url(url: str):
  short_code = generate_short_code()
  date = convert_datetime_to_json(datetime.now())

  data = supabase_database.table("url-table").insert({
    "url": url,
    "shortcode": short_code,
    "updated_at": date,
  }).execute()

  return data.data[0]


if __name__ == "__main__":
  results = supabase_database.table("url-table").select("*").execute()
  print(results)