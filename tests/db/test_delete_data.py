import pytest, random, string

from app.db import database
from tests.core.dummy_database import DummyClient, DummyTable
from tests.core.dummy_table_data import dummy_table_data

def test_delete_data_success(monkeypatch):
  first_id = 1
  second_id = 3

  monkeypatch.setattr(
    database,
    "supabase_database",
    DummyClient(DummyTable(None, None, all_data = dummy_table_data))
  )

  first_result = database.delete_url(first_id)
  second_result = database.delete_url(second_id)

  assert first_result is not None
  assert second_result is not None

@pytest.mark.parametrize(
  ("bad_input", "error_message"),
  [
    (random.choice(string.ascii_letters), "Characters can't be used as an Id"),
    (random.choice(string.punctuation), "Characters can't be used as an Id")
  ],
)

def test_delete_data_error(monkeypatch, bad_input, error_message):
  monkeypatch.setattr(
    database,
    "supabase_database",
    DummyClient(DummyTable(None, None, all_data = dummy_table_data))
  )

  with pytest.raises(TypeError, match=error_message):
    database.delete_url(bad_input)

  assert not database.delete_url(10)