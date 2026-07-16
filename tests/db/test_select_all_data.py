import pytest
from app.db import database
from tests.core.dummy_database import DummyClient, DummyTable

def test_select_all_url_success(monkeypatch):
  monkeypatch.setattr(database, "supabase_database", DummyClient(DummyTable()))