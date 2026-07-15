import pytest
from app.db import database
from tests.core.dummy_database import DummyClient, DummyTable


def test_insert_url_success(monkeypatch):
    url = "https://github.com/Muelvzz/url-shortening-service"
    short_url = "https://tinyurl.com/short123"

    def fake_create_short_url(value):
        assert value == url
        return short_url

    monkeypatch.setattr(database, "create_short_url", fake_create_short_url)
    monkeypatch.setattr(database, "supabase_database", DummyClient(DummyTable(url, short_url)))

    result = database.insert_url(url)

    assert result["url"] == url
    assert result["short_url"] == short_url
    assert isinstance(result["updated_at"], str)


@pytest.mark.parametrize(
    "bad_input, error_message",
    [
        ("", "empty"),
        ("https://tinyurl.com/abc123", "already a shortened"),
    ],
)

def test_insert_url_validation_errors(monkeypatch, bad_input, error_message):
    def fake_create_short_url(value):
        if not value:
            raise ValueError("The provided URL is empty.")
        raise ValueError("The provided URL is already a shortened URL.")

    monkeypatch.setattr(database, "create_short_url", fake_create_short_url)

    with pytest.raises(ValueError, match=error_message):
        database.insert_url(bad_input)


def test_insert_url_database_failure(monkeypatch):
    url = "https://github.com/Muelvzz/url-shortening-service"
    short_url = "https://tinyurl.com/short123"

    def fake_create_short_url(value):
        return short_url

    class BrokenTable:
        def insert(self, row):
            raise RuntimeError("Supabase unavailable")

    monkeypatch.setattr(database, "create_short_url", fake_create_short_url)
    monkeypatch.setattr(database, "supabase_database", DummyClient(BrokenTable()))

    with pytest.raises(RuntimeError, match="Supabase unavailable"):
        database.insert_url(url)