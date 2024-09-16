import hashlib
import base64
from urllib.parse import urlparse
from storage import save_data, get_original_url

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def shorten_url(url, id_length=8):
    if not is_valid_url(url):
        return None, "Invalid URL"

    # Create a SHA-256 hash of the URL
    url_hash = hashlib.sha256(url.encode()).digest()
    
    # Convert the hash to a URL-safe base64 string
    base64_encoded = base64.urlsafe_b64encode(url_hash).decode('utf-8')
    
    # Take the first `id_length` characters as the short ID
    short_id = base64_encoded[:id_length]
    
    # Save the mapping
    save_success = save_data(url, short_id)
    if not save_success:
        return None, "Failed to save URL"

    # You can customize the base URL as needed
    base_url = "https://myApp.com/"
    
    # Return the shortened URL and the base64-encoded hash (hash key)
    return f"{base_url}{short_id}", base64_encoded, None

def expand_url(short_url):
    # Extract the short ID from the URL
    short_id = short_url.split("/")[-1]
    
    # Get the original URL
    original_url = get_original_url(short_id)
    if original_url is None:
        return None, "URL not found"
    
    return original_url, None

def count_urls():
    from storage import get_data
    return len(get_data())
