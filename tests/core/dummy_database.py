class DummyInsertResult:
    def __init__(self, row):
        self.data = [row]

    def execute(self):
        return self


class DummyTable:
    def __init__(self, expected_url, expected_short_url):
        self.expected_url = expected_url
        self.expected_short_url = expected_short_url

    def insert(self, row):
        assert row["url"] == self.expected_url
        assert row["short_url"] == self.expected_short_url
        assert "updated_at" in row
        return DummyInsertResult(row)


class DummyClient:
    def __init__(self, table):
        self._table = table

    def table(self, name):
        assert name == "url-table"
        return self._table