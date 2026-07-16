from .dummy_table_data import dummy_table_data
from ...app.db.database import view_all_urls

class DummyInsertResult:
    def __init__(self, row):
        self.data = [row]

    def execute(self):
        return self


class DummyViewAllResult:
    def __init(self, data: list):
        self.data = data

    def execute(self): 
        return self
    
    def select(self, id: int | None):
        return self.data[id]

class DummyTable:
    def __init__(
            self, 
            expected_url: str | None, 
            expected_short_url: str | None, 
            all_data = dummy_table_data
        ):
        self.expected_url = expected_url
        self.expected_short_url = expected_short_url

    def insert(self, row):
        assert row["url"] == self.expected_url
        assert row["short_url"] == self.expected_short_url
        assert "updated_at" in row
        return DummyInsertResult(row)
    
    def view_all():
        pass


class DummyClient:
    def __init__(self, table):
        self._table = table

    def table(self, name):
        assert name == "url-table"
        return self._table