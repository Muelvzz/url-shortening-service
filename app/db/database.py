from supabase import create_client, Client

from app.core import config

supabase: Client = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)

results = supabase.table("url-table").select("*").execute()

if __name__ == "__main__":
  print(results)