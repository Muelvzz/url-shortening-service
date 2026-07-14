import pyshorteners

init_url_shortener = pyshorteners.Shortener()

def create_short_url(url):
  shortened_url = init_url_shortener.tinyurl.short(url)

  return shortened_url
  

if __name__ == "__main__":
  short_url = create_short_url()
  print(f"Short URL: {short_url}")