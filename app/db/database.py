from ..core.config import supabase_database
from ..utils.short_url import create_short_url
from ..utils.datetime_json import convert_datetime_to_json
from ..utils.validate_url import validate_url
from datetime import datetime

def insert_url(url: str):
    url = validate_url(url)
    short_url = create_short_url(url)
    date = convert_datetime_to_json(datetime.now())

    try:
        data = supabase_database.table("url-table").insert({
            "url": url,
            "short_url": short_url,
            "updated_at": date,
        }).execute()
        
    except Exception as e:
        raise RuntimeError(
            f"Error occurred while inserting the URL into the database: {e}"
        ) from e

    if not getattr(data, "data", None) or len(data.data) == 0:
        raise RuntimeError("Database insert returned no row data.")

    return data.data[0]


if __name__ == "__main__":
    results = supabase_database.table("*").select("*").execute()
    print(results)