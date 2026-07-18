from ..core.config import supabase_database
from ..utils.short_url import create_short_url
from ..utils.datetime_json import convert_datetime_to_json
from ..utils.validate_url import validate_url
from datetime import datetime

def check_id(id: int):
    if isinstance(id, bool) or not isinstance(id, int):
        raise TypeError("Characters can't be used as an Id")
    
    return id

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
    checked_id = check_id(id)

    try:
       select_data = (supabase_database.table("url-table").select("*").eq("id", checked_id).maybe_single().execute())

    except Exception as e:
        raise RuntimeError(
            f"Error occured while retrieving the selected url: {e}"
        ) from e
    
    if select_data is None:
        raise RuntimeError(f"Id {checked_id} could not be found.")
    
    return select_data.data

def delete_url(id: int):
    checked_id = check_id(id)

    try:
        deleted_data = (supabase_database.table("url-table").delete().eq("id", checked_id).execute())

    except Exception as e:
        raise RuntimeError(
            f"Error occured while deleting the url: {e}"
        ) from e
    
    if not getattr(deleted_data, "data", None):
        raise RuntimeError(f"Id {checked_id} could not be found.")

    if isinstance(deleted_data.data, list):
        return deleted_data.data[0] if deleted_data.data else None

    return deleted_data.data


if __name__ == "__main__":
    results = supabase_database.table("url-table").select("*").execute()
    print(results)