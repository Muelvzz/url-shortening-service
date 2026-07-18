from .dummy_table_data import dummy_table_data

class DummyInsertResult:
    def __init__(self, row):
        self.data = [row]

    def execute(self):
        return self


class DummySelectResult:
    def __init__(self, data: list):
        self.data = data

    def eq(self, column, value):
        if column == "id":
            self.data = [row for row in self.data if row.get("id") == value]
        return self

    def execute(self): 
        return self
    
    def single(self):
        return self

    def maybe_single(self):
        return self
    
class DummyDeleteResult:
    def __init__(self, all_data: list = dummy_table_data):
        self.id = None
        self.all_data = all_data

    def eq(self, column, value):
        if column == "id":
            self.id = value
        return self

    def execute(self):
        if self.id is None:
            raise ValueError("No Id provided")
        
        for index, row in enumerate(self.all_data):
            if row.get("id") == self.id:
                return self.all_data.pop(index)
            
        raise KeyError(f"Id {self.id} could not be found")

class DummyTable:
    def __init__(
            self, 
            expected_url: str, 
            expected_short_url: str, 
            all_data: list = None,
        ):
        self.expected_url = expected_url
        self.expected_short_url = expected_short_url
        self.all_data = dummy_table_data if all_data is None else all_data

    def insert(self, row):
        assert row["url"] == self.expected_url
        assert row["short_url"] == self.expected_short_url
        assert "updated_at" in row
        return DummyInsertResult(row)
    
    def select(self, 
               *_args, 
               **_kwargs
            ):
        return DummySelectResult(self.all_data)
    
    def delete(self,
               *_args, 
               **_kwargs
            ):
        return DummyDeleteResult(self.all_data)


class DummyClient:
    def __init__(self, table):
        self._table = table

    def table(self, name):
        if name not in {"url-table", "*"}:
            raise AssertionError(f"Unexpected table name: {name}")
        return self._table