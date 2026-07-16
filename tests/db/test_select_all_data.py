from app.db import database
from tests.core.dummy_database import DummyClient, DummyTable
from tests.core.dummy_table_data import dummy_table_data

def test_select_all_url_success(monkeypatch):
  monkeypatch.setattr(
    database, 
    "supabase_database", 
    DummyClient(DummyTable(None, None, all_data = dummy_table_data))
  )

  result = database.view_all_urls()
  
  assert result is not None
  assert result.data == dummy_table_data
  assert len(result.data) == len(dummy_table_data)