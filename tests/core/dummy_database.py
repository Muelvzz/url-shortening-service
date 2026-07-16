from .dummy_table_data import dummy_table_data

class DummyInsertResult:
    def __init__(self, row):
        self.data = [row]

    def execute(self):
        return self


class DummySelectResult:
    def __init__(self, data: list):
        self.data = data

    def execute(self): 
        return self
    
    def select(self, id: int | None):
        return self.data[id]

class DummyTable:
    def __init__(
            self, 
            expected_url: str, 
            expected_short_url: str, 
            all_data = None
        ):
        self.expected_url = expected_url
        self.expected_short_url = expected_short_url
        self.all_data = dummy_table_data if all_data is None else all_data

    def insert(self, row):
        assert row["url"] == self.expected_url
        assert row["short_url"] == self.expected_short_url
        assert "updated_at" in row
        return DummyInsertResult(row)
    
    def select(self, *_args, **_kwargs):
        return DummySelectResult(self.all_data)


class DummyClient:
    def __init__(self, table):
        self._table = table

    def table(self, name):
        if name not in {"url-table", "*"}:
            raise AssertionError(f"Unexpected table name: {name}")
        return self._table