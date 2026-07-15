from urllib.parse import urlparse

def validate_url(url: str):
    if url is None:
        raise ValueError("The provided URL is None.")
    if not isinstance(url, str) or not url.strip():
        raise ValueError("The provided URL is empty.")

    cleaned = url.strip()
    parsed = urlparse(cleaned)

    if not parsed.scheme or not parsed.netloc:
        raise ValueError("The provided URL is invalid.")

    return cleaned