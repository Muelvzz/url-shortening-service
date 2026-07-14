import pytest
from app.utils.short_url import create_short_url

def test_get_short_url():
  url_one = "https://github.com/Muelvzz/url-shortening-service"
  url_two = "https://tinyurl.com/abc123"

  testing_one = create_short_url(url_one)

  assert testing_one.startswith("http")
  assert testing_one != url_one

  with pytest.raises(ValueError):
    create_short_url(url_two)

  with pytest.raises(ValueError):
    create_short_url("")