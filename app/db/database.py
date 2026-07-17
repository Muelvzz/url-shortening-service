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

def view_all_urls():
    try:
        all_data = supabase_database.table("url-table").select("*").execute()

    except Exception as e:
        raise RuntimeError(
            f"Error occured while fetching all the URL into the database: {e}"
        ) from e
    
    if not getattr(all_data, "data", None) or len(all_data.data) == 0:
        raise RuntimeError("There are no existing data.")
    
    return all_data.data

def view_selected_url(id: int):
    try:
       select_data = supabase_database.table("url-table").select("*").eq("id", id).single().execute() 

    except Exception as e:
        raise RuntimeError(
            f"Error occured while retrieving the selected url: {e}"
        ) from e
    
    if not getattr(select_data, "data", None) or len(select_data.data) == 0:
        raise RuntimeError(f"Id {id} could not found.")
    
    return select_data.data


if __name__ == "__main__":
    results = supabase_database.table("url-table").select("*").execute()
    print(results)