import pyshorteners

init_url_shortener = pyshorteners.Shortener()

def create_short_url(url):
  if "tinyurl.com" in url:
    raise ValueError("The provided URL is already a shortened URL.")

  if not url:
    raise ValueError("The provided URL is empty.")
  
  shortened_url = init_url_shortener.tinyurl.short(url)

  return shortened_url